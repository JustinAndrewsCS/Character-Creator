-- Resets database if it already exists
DROP DATABASE IF EXISTS games;
CREATE DATABASE IF NOT EXISTS games;
use games;


-- Create the Tables

-- Games(GameID, Title)
CREATE TABLE Games(
	gameID INT,
	title VARCHAR(60),
    PRIMARY KEY(gameID)
);


-- Character(CharID, class, charName, sex, strength, dexterity, constitution, 
--           intelligence, widsdom, charisma, treatInjury, computerUse,
--           demolitions, stealth, awareness, persuade, repair, security)
CREATE TABLE Characters(
	charID INT,
	class VARCHAR(12),
	charName VARCHAR(30),
    sex VARCHAR(10),
    strength INT,
    dexterity INT,
    constitution INT,
    intelligence INT,
    wisdom INT,
    charisma INT,
    treatInjury INT,
    computerUse INT,
    demolitions INT,
    stealth INT,
    awareness INT,
    persuade INT,
    repairSkill INT,
    securitySkill INT,
    gameID INT,
    PRIMARY KEY(charID)
);


-- ------------------------------------------------
-- Insert Data
INSERT INTO Games VALUES 
	(1000, 'Star Wars')
    ;
    
INSERT INTO Characters VALUES
	(1000, 'test', 'testChar', 'test', 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1000)
    ;