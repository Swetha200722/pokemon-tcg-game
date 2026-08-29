CREATE TABLE cards (
    card_id SERIAL PRIMARY KEY,
    card_name VARCHAR(100) NOT NULL,
    card_type VARCHAR(50) NOT NULL,
    pokemon_type VARCHAR(50),
    hp INTEGER,
    attack_name VARCHAR(100),
    attack_damage INTEGER
);

CREATE TABLE players (
    player_id SERIAL PRIMARY KEY,
    player_name VARCHAR(100) NOT NULL
);

CREATE TABLE decks (
    deck_id SERIAL PRIMARY KEY,
    deck_name VARCHAR(100) NOT NULL,
    player_id INTEGER REFERENCES players(player_id)
);

CREATE TABLE games (
    game_id SERIAL PRIMARY KEY,
    player1_id INTEGER REFERENCES players(player_id),
    player2_id INTEGER REFERENCES players(player_id),
    winner_id INTEGER REFERENCES players(player_id),
    total_turns INTEGER
);

CREATE TABLE game_actions (
    action_id SERIAL PRIMARY KEY,
    game_id INTEGER REFERENCES games(game_id),
    turn_number INTEGER,
    player_id INTEGER REFERENCES players(player_id),
    action_type VARCHAR(50),
    card_id INTEGER REFERENCES cards(card_id)
);