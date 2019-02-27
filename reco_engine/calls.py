from cypher_commands import tx__get_rated_games, tx__get_recommendations, tx__rate_game
from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://hobby-djmhmmpijhligbkengololcl.dbs.graphenedb.com:24786", auth=("admin", "b.xhxpEtHblPLD.Z4yruirvyneIegGA"))


def get_rated_games():
	pass

def get_recommendations(user_name):

	with driver.session() as session:
		response = session.read_transaction(
			tx__get_recommendations,
			user_name=user_name
			)
		print(response)


def rate_game(user_id, game_psid, game_name, game_thumbnail, rating):

	with driver.session() as session:
		response = session.write_transaction(
			tx__rate_game,
			user_id=user_id,
			game_psid=game_psid,
			game_name=game_name,
			game_thumbnail=game_thumbnail,
			rating=rating,
			)
		print(response)


rate_game(
	rating=1,
	user_id="TEST_USER",
	game_psid="marcostudios.lovetest",
	game_name="Test d'Amour",
	game_thumbnail="//lh3.googleusercontent.com/ppcIvoWWD4VZYZkrEnFXHvEWjdMsRpItRAaZlT_wvR45vqM-9yAKRFvUDc7L1W9bw1HU=w170",
	)