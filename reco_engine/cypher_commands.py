def tx__get_rated_games(tx, user_name, rating=None):
    if rating in [1,2,3,4]:
        print("With rating", rating)
        response = tx.run(
            '''
            MATCH (u:User {name: $user_name})-[:RATED {rating: $rating}]->(g:Game)
            RETURN g
            ''',
            user_name=user_name, rating=rating
            )
    else:
        response = tx.run(
            '''
            MATCH (u:User {name: $user_name})-[:RATED]->(g:Game)
            RETURN g
            ''',
            user_name=user_name
            )
    for record in response:
        game = record["g"]
        return(game._properties['name'])

def tx__get_recommendations(tx, user_name):
    response = tx.run(
        '''
        MATCH (p1:User {name: $user_name})-[x]->(g:Game)<-[y]-(p2:User)
        WITH COUNT(x) AS numbergames, SUM(x.rating * y.rating) AS xyDotProduct,
        SQRT(REDUCE(xDot = 0.0, a IN COLLECT(x.rating) | xDot + a^2)) AS xLength,
        SQRT(REDUCE(yDot = 0.0, b IN COLLECT(y.rating) | yDot + b^2)) AS yLength,
        p1, p2 WHERE numbergames > 3
        MATCH (p2)-[:RATED {rating: 4}]->(rec:Game) WHERE NOT EXISTS ((p1)-[]->(rec))
        RETURN p1.name, p2.name, xyDotProduct / (xLength * yLength) AS sim, rec.name
        ORDER BY sim DESC LIMIT 3
        ''',
        user_name=user_name
        )
    return list(map(lambda record: record["rec.name"], response))
#        return(game._properties['name'])


def tx__rate_game(tx, **kwargs):
    response = tx.run(
        '''
        MERGE (g:Game {psid: $game_psid, name: $game_name, thumbnail: $game_thumbnail})
        MERGE (u:User {name: $user_id})
        CREATE (u)-[r:RATED {rating : "$rating"}]->(g)
        RETURN u, r, g
        ''', **kwargs
        )
    return list(map(lambda record: record["u"], response))
