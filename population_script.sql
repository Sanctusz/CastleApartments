INSERT INTO agents_agents (name, email, phone, description, image) VALUES('Lydia of Whiterun','lydia@housecarl.sky','7759930','She has a strong sense of justice and a strong aptitude for plowing through attackers with her fierce swordsmanship.','https://oyster.ignimgs.com/mediawiki/apis.ign.com/the-elder-scrolls-5-skyrim/6/68/Lydia.jpg?width=960');
INSERT INTO agents_agents (name, email, phone, description, image) VALUES('Jordis the Sword-Maiden of Solitude','jordis@housecarl.sky','77586930','Jordis is a loyal Housecarl to the Thane of Haafingar.','https://oyster.ignimgs.com/mediawiki/apis.ign.com/the-elder-scrolls-5-skyrim/3/3e/SR_Jordis.jpg?width=640');
INSERT INTO agents_agents (name, email, phone, description, image) VALUES('Calder of Windhelm','Calder@housecarl.sky','7779930','Like other Housecarls, he is a proficient tank with expertise in Heavy Armor, Block, One-Handed, and Archery.','https://oyster.ignimgs.com/mediawiki/apis.ign.com/the-elder-scrolls-5-skyrim/9/91/Calder.png?width=640');


INSERT INTO properties_propertiesaddress("streetName","houseNumber","zipCode",city,country) VALUES('Breezehome',35,400,'Whiterun','Skyrim');
INSERT INTO properties_propertiesaddress("streetName","houseNumber","zipCode",city,country) VALUES('Hjerim',46,300,'Windhelm','Skyrim');
INSERT INTO properties_propertiesaddress("streetName","houseNumber","zipCode",city,country) VALUES('Honeyside',65,260,'Riften','Skyrim');
INSERT INTO properties_propertiesaddress("streetName","houseNumber","zipCode",city,country) VALUES('Proudspire Manor',120,700,'Solitude','Skyrim');
INSERT INTO properties_propertiesdetails(garden,garage,pets,accessibility) VALUES(false,false,true,true);
INSERT INTO properties_propertiesdetails(garden,garage,pets,accessibility) VALUES(true,false,true,true);
INSERT INTO properties_propertiesdetails(garden,garage,pets,accessibility) VALUES(true,false,true,false);
INSERT INTO properties_propertiesdetails(garden,garage,pets,accessibility) VALUES(true,true,true,true);
INSERT INTO properties_properties (type, size, room, price, "yearBuilt", description, status, agent_id, details_id, address_id) VALUES('house',245,4,5000000,1986,'Located in Whiterun, Breezehome sits adjacent to Warmaidens and Whiteruns Gate.Physically, it resembles many of the other houses of Whiterun, with pale wooden walls, a few windows and a shingled roof.','available',1,17,18);
INSERT INTO properties_properties (type, size, room, price, "yearBuilt", description, status, agent_id, details_id, address_id) VALUES('house',456,7,12000000,1995,'It is located in the Valunstrad quarter of Windhelm. The house has two floors, several spacious rooms and a hidden chamber. Hjerim also has a large armory with a number of mannequins, display cases, shelves, and weapon racks.','available',2,18,19);
INSERT INTO properties_properties (type, size, room, price, "yearBuilt", description, status, agent_id, details_id, address_id) VALUES('house',534,5,8000000,1988,'With its exterior entry, tanning rack, cooking place, alchemy lab, and arcane enchanter, Honeyside can be a useful home for hunters and those who are interested in alchemy or enchanting.','available',3,19,20);
INSERT INTO properties_properties (type, size, room, price, "yearBuilt", description, status, agent_id, details_id, address_id) VALUES('house',643,10,36000000,1998,'Proudspire Manor is the door before the brazier. It can also be accessed by going up the steps before that doorway; Vittoria Vicis house is the door to the left, while Proudspire Manor is the door on the right. The exterior of the manor has a fair amount of flowers that respawn in a few game weeks if picked.','available',1,20,21);
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/elderscrolls/images/7/7a/Hjerim_House.png/revision/latest/scale-to-width-down/1000?cb=20141014123212', 11, 'mynd 3');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/elderscrolls/images/1/19/Honeyside.jpg/revision/latest?cb=20120227003816', 12, 'mynd 4');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/elderscrolls/images/8/87/Proudspire_Manor.jpg/revision/latest/scale-to-width-down/1000?cb=20111128231658', 13, 'mynd 5');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/elderscrolls/images/7/72/Breezhome_Improved.png/revision/latest/scale-to-width-down/1000?cb=20130118014012', 14, 'mynd 2');