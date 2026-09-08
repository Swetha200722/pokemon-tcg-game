from fastapi import FastAPI, HTTPException
import psycopg2

app = FastAPI(title="Pokemon TCG API")


def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="pokemon_tcg",
        user="postgres",
        password="Swetha@123"
    )


# -------------------------
# HOME
# -------------------------

@app.get("/")
def home():
    return {"message": "Pokemon TCG API is running"}


# -------------------------
# CARDS
# -------------------------

@app.get("/cards")
def get_cards():
    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                card_id,
                card_name,
                card_type,
                pokemon_type,
                hp,
                attack_name,
                attack_damage
            FROM cards
            ORDER BY card_id;
        """)

        rows = cursor.fetchall()

        return [
            {
                "card_id": row[0],
                "card_name": row[1],
                "card_type": row[2],
                "pokemon_type": row[3],
                "hp": row[4],
                "attack_name": row[5],
                "attack_damage": row[6],
            }
            for row in rows
        ]

    finally:
        conn.close()


# -------------------------
# PLAYERS
# -------------------------

@app.get("/players")
def get_players():
    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT player_id, player_name
            FROM players
            ORDER BY player_id;
        """)

        rows = cursor.fetchall()

        return [
            {
                "player_id": row[0],
                "player_name": row[1]
            }
            for row in rows
        ]

    finally:
        conn.close()


# -------------------------
# DECKS
# -------------------------

@app.get("/decks")
def get_decks():
    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT deck_id, deck_name, player_id
            FROM decks
            ORDER BY deck_id;
        """)

        rows = cursor.fetchall()

        return [
            {
                "deck_id": row[0],
                "deck_name": row[1],
                "player_id": row[2]
            }
            for row in rows
        ]

    finally:
        conn.close()


# -------------------------
# GAMES
# -------------------------

@app.get("/games")
def get_games():
    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                game_id,
                player1_id,
                player2_id,
                winner_id,
                total_turns
            FROM games
            ORDER BY game_id;
        """)

        rows = cursor.fetchall()

        return [
            {
                "game_id": row[0],
                "player1_id": row[1],
                "player2_id": row[2],
                "winner_id": row[3],
                "total_turns": row[4]
            }
            for row in rows
        ]

    finally:
        conn.close()


# -------------------------
# GAME ACTIONS
# -------------------------

@app.get("/games/{game_id}/actions")
def get_game_actions(game_id: int):
    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                action_id,
                game_id,
                turn_number,
                player_id,
                action_type,
                card_id
            FROM game_actions
            WHERE game_id = %s
            ORDER BY turn_number;
        """, (game_id,))

        rows = cursor.fetchall()

        return [
            {
                "action_id": row[0],
                "game_id": row[1],
                "turn_number": row[2],
                "player_id": row[3],
                "action_type": row[4],
                "card_id": row[5]
            }
            for row in rows
        ]

    finally:
        conn.close()


# -------------------------
# GAME STATES
# -------------------------

@app.get("/games/{game_id}/states")
def get_game_states(game_id: int):
    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                state_id,
                game_id,
                turn_number,
                player_id,
                active_card_id,
                opponent_active_card_id,
                player_hp,
                opponent_hp,
                player_prizes,
                opponent_prizes,
                player_energy,
                opponent_energy
            FROM game_states
            WHERE game_id = %s
            ORDER BY turn_number;
        """, (game_id,))

        rows = cursor.fetchall()

        return [
            {
                "state_id": row[0],
                "game_id": row[1],
                "turn_number": row[2],
                "player_id": row[3],
                "active_card_id": row[4],
                "opponent_active_card_id": row[5],
                "player_hp": row[6],
                "opponent_hp": row[7],
                "player_prizes": row[8],
                "opponent_prizes": row[9],
                "player_energy": row[10],
                "opponent_energy": row[11]
            }
            for row in rows
        ]

    finally:
        conn.close()


# -------------------------
# BATTLE RESULTS
# -------------------------

@app.get("/battle-results")
def get_battle_results():
    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                result_id,
                game_id,
                winner_id,
                loser_id,
                winner_prizes_remaining,
                loser_prizes_remaining,
                total_turns,
                winning_strategy
            FROM battle_results
            ORDER BY result_id;
        """)

        rows = cursor.fetchall()

        return [
            {
                "result_id": row[0],
                "game_id": row[1],
                "winner_id": row[2],
                "loser_id": row[3],
                "winner_prizes_remaining": row[4],
                "loser_prizes_remaining": row[5],
                "total_turns": row[6],
                "winning_strategy": row[7]
            }
            for row in rows
        ]

    finally:
        conn.close()