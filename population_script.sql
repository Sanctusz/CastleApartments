/*Skyrim */
INSERT INTO agents_agents (name, email, phone, description, image) VALUES('Lydia of Whiterun','lydia@housecarl.sky','7759930','She has a strong sense of justice and a strong aptitude for plowing through attackers with her fierce swordsmanship.','https://oyster.ignimgs.com/mediawiki/apis.ign.com/the-elder-scrolls-5-skyrim/6/68/Lydia.jpg?width=960');
INSERT INTO agents_agents (name, email, phone, description, image) VALUES('Jordis the Sword-Maiden of Solitude','jordis@housecarl.sky','77586930','Jordis is a loyal Housecarl to the Thane of Haafingar.','https://oyster.ignimgs.com/mediawiki/apis.ign.com/the-elder-scrolls-5-skyrim/3/3e/SR_Jordis.jpg?width=640');
INSERT INTO agents_agents (name, email, phone, description, image) VALUES('Calder of Windhelm','calder@housecarl.sky','7779930','Like other Housecarls, he is a proficient tank with expertise in Heavy Armor, Block, One-Handed, and Archery.','https://oyster.ignimgs.com/mediawiki/apis.ign.com/the-elder-scrolls-5-skyrim/9/91/Calder.png?width=640');
/*Fallout */
INSERT INTO agents_agents (name, email, phone, description, image) VALUES('Chosen One','chosen@vaultdweller.fall','8899930','The Chosen One was trained from birth to become the tribe''s champion and, in the future, their elder. ','https://vignette.wikia.nocookie.net/fallout/images/7/7d/Chosen_One_Car.jpg/revision/latest?cb=20090720172204');
INSERT INTO agents_agents (name, email, phone, description, image) VALUES('Lone Wanderer','wanderer@vaultdweller.fall','8779830','The Lone Wanderer lived in Vault 101 without incident for nineteen years, but in 2277, two hundred years after the Great War he had to leave the safety of vault','https://vignette.wikia.nocookie.net/fallout/images/2/2e/Lone_Wanderer.jpg/revision/latest?cb=20150510133635');
INSERT INTO agents_agents (name, email, phone, description, image) VALUES('Sole Survivor','survivor@vaultdweller.fall','8788930','Sole survivor is law school graduate.She was sealed in cryogenic stasis under the pretense of being "decontaminated" by Vault-Tec scientists. The Sole Survivor is kept almost undisturbed in this state from 2077 to 2287.','https://wallpapersite.com/images/pages/pic_h/224.jpg');
/* bioshock infinite */
INSERT INTO agents_agents (name, email, phone, description, image) VALUES('Booker DeWitt','dewitt@bio.shock','9797930','Booker DeWitt is an experienced detective and former U.S. Army Cavalry soldier. This has given him the skill set needed to survive his trip to Columbia. Most apparent of these skills are his combat abilities.','https://vignette.wikia.nocookie.net/bioshock/images/7/75/Bioshockinfiniteartworks7.jpg/revision/latest?cb=20130208122619');
INSERT INTO agents_agents (name, email, phone, description, image) VALUES('Elizabeth','elizabeth@bio.shock','9778990','Elizabeth is gifted (or cursed) with the ability to manipulate Tears, contingencies within the space-time continuum that show possible scenarios which, if tampered with, can enact themselves within Columbia or any universe in particular.','https://vignette.wikia.nocookie.net/bioshock/images/0/07/Elizabeth-C.png/revision/latest?cb=20130501031608');
INSERT INTO agents_agents (name, email, phone, description, image) VALUES('Songbird','songbird@bio.shock','9977830','The Songbird was created by Fink Manufacturing and like most of Jeremiah Fink''s technology, it was based on designs discovered through a Tear.','https://vignette.wikia.nocookie.net/bioshock/images/4/4e/Songbird_header-864x1024.jpg/revision/latest?cb=20130404083839');

/*skyrim*/
INSERT INTO properties_propertiesaddress("streetName","houseNumber","zipCode",city,country) VALUES('Breezehome',35,400,'Whiterun','Skyrim');
INSERT INTO properties_propertiesaddress("streetName","houseNumber","zipCode",city,country) VALUES('Hjerim',46,300,'Windhelm','Skyrim');
INSERT INTO properties_propertiesaddress("streetName","houseNumber","zipCode",city,country) VALUES('Honeyside',65,260,'Riften','Skyrim');
INSERT INTO properties_propertiesaddress("streetName","houseNumber","zipCode",city,country) VALUES('Proudspire Manor',120,700,'Solitude','Skyrim');
INSERT INTO properties_propertiesdetails(garden,garage,pets,accessibility) VALUES(false,false,true,true);
INSERT INTO properties_propertiesdetails(garden,garage,pets,accessibility) VALUES(true,false,true,true);
INSERT INTO properties_propertiesdetails(garden,garage,pets,accessibility) VALUES(true,false,true,false);
INSERT INTO properties_propertiesdetails(garden,garage,pets,accessibility) VALUES(true,true,true,true);
INSERT INTO properties_properties (type, size, rooms, price, "yearBuilt", description, status, agent_id, details_id, address_id) VALUES('house',245,4,5000000,1986,'Located in Whiterun, Breezehome sits adjacent to Warmaidens and Whiteruns Gate.Physically, it resembles many of the other houses of Whiterun, with pale wooden walls, a few windows and a shingled roof.','available',1,1,1);
INSERT INTO properties_properties (type, size, rooms, price, "yearBuilt", description, status, agent_id, details_id, address_id) VALUES('house',456,7,12000000,1995,'It is located in the Valunstrad quarter of Windhelm. The house has two floors, several spacious rooms and a hidden chamber. Hjerim also has a large armory with a number of mannequins, display cases, shelves, and weapon racks.','available',2,2,2);
INSERT INTO properties_properties (type, size, rooms, price, "yearBuilt", description, status, agent_id, details_id, address_id) VALUES('house',534,5,8000000,1988,'With its exterior entry, tanning rack, cooking place, alchemy lab, and arcane enchanter, Honeyside can be a useful home for hunters and those who are interested in alchemy or enchanting.','available',3,3,3);
INSERT INTO properties_properties (type, size, rooms, price, "yearBuilt", description, status, agent_id, details_id, address_id) VALUES('house',643,10,36000000,1998,'Proudspire Manor is the door before the brazier. It can also be accessed by going up the steps before that doorway; Vittoria Vicis house is the door to the left, while Proudspire Manor is the door on the right. The exterior of the manor has a fair amount of flowers that respawn in a few game weeks if picked.','available',1,4,4);
/* house 1 skyrim*/
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/elderscrolls/images/7/72/Breezhome_Improved.png/revision/latest?cb=20130118014012', 1, 'mynd 1');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/elderscrolls/images/0/0e/Breezehome_-_entrance.jpg/revision/latest/scale-to-width-down/640?cb=20111118162124', 1, 'mynd 2');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/elderscrolls/images/4/47/Breezehome01.jpg/revision/latest?cb=20111118162229', 1, 'mynd 3');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/elderscrolls/images/6/6f/Breezehome_-_Child%27s_Bedroom.png/revision/latest?cb=20121005035132', 1, 'mynd 4');
/* house 2 skyrim */
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/elderscrolls/images/7/7a/Hjerim_House.png/revision/latest?cb=20141014123212', 2, 'mynd 5');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/elderscrolls/images/8/85/HjerimKitchen.jpg/revision/latest?cb=20111116153516', 2, 'mynd 6');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/elderscrolls/images/3/38/HjerimLivingRoom.jpg/revision/latest?cb=20111116153539', 2, 'mynd 7');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/elderscrolls/images/0/02/Hjerim_-_Child%27s_Bedroom.png/revision/latest?cb=20121005035132', 2, 'mynd 8');
/* house 3 skyrim*/
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/elderscrolls/images/1/19/Honeyside.jpg/revision/latest?cb=20120227003816', 3, 'mynd 9');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/elderscrolls/images/6/68/Honeyside_porch.png/revision/latest?cb=20121109235821', 3, 'mynd 10');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/elderscrolls/images/3/39/Honeyside_garden.png/revision/latest?cb=20121109235740', 3, 'mynd 11');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/elderscrolls/images/8/82/Honeyside_bedroom.png/revision/latest?cb=20121109235657', 3, 'mynd 12');
/* house 4 skyrim */
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/elderscrolls/images/8/87/Proudspire_Manor.jpg/revision/latest?cb=20111128231658', 4, 'mynd 13');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/elderscrolls/images/6/66/ProudspireManorBedroomPreUpgrade.jpg/revision/latest?cb=20111115155938', 4, 'mynd 14');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/elderscrolls/images/4/4e/Proudspire_Manor_-_first_floor_-_door_to_patio.jpg/revision/latest?cb=20111118160809', 4, 'mynd 15');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/elderscrolls/images/2/24/Proudspire_Manor_-_first_flor_entrance.jpg/revision/latest?cb=20111118160918', 4, 'mynd 16');
/*fallout*/
INSERT INTO properties_propertiesaddress("streetName","houseNumber","zipCode",city,country) VALUES('Vault',111,101,'Sanctuary Hills','Fallout');
INSERT INTO properties_propertiesaddress("streetName","houseNumber","zipCode",city,country) VALUES('Vault',95,110,'Commonwealth','Fallout');
INSERT INTO properties_propertiesaddress("streetName","houseNumber","zipCode",city,country) VALUES('Vault',3,112,'Mojave Wasteland','Fallout');
INSERT INTO properties_propertiesaddress("streetName","houseNumber","zipCode",city,country) VALUES('Vault',34,112,'Mojave Wasteland.','Fallout');
INSERT INTO properties_propertiesdetails(garden,garage,pets,accessibility) VALUES(true,false,true,true);
INSERT INTO properties_propertiesdetails(garden,garage,pets,accessibility) VALUES(true,true,true,true);
INSERT INTO properties_propertiesdetails(garden,garage,pets,accessibility) VALUES(true,false,true,false);
INSERT INTO properties_propertiesdetails(garden,garage,pets,accessibility) VALUES(true,false,true,true);
INSERT INTO properties_properties (type, size, rooms, price, "yearBuilt", description, status, agent_id, details_id, address_id) VALUES('apartment',110,3,14000000,2011,'Vault-Tec designed Vault 111 to observe the effects of long-term cryogenic suspended animation on unsuspecting test subjects. Vault 111''s staff consisted of an overseer and a small team of scientists, security guards and facility maintenance personnel employed on a short-term basis.','available',6,5,5);
INSERT INTO properties_properties (type, size, rooms, price, "yearBuilt", description, status, agent_id, details_id, address_id) VALUES('apartment',89,2,10000000,2010,' The vault proper has three separate sections: the south side with the cafeteria and detox chamber, the west side with the reactor down below and the Overseer''s office above, and the north side containing a heavily trapped tunnel that leads to the residential area.','available',4,6,6);
INSERT INTO properties_properties (type, size, rooms, price, "yearBuilt", description, status, agent_id, details_id, address_id) VALUES('apartment',97,2,11500000,2001,'In many ways, Vault 3 was the ideal post-apocalyptic community that had all too often evaded Vault-Tec''s many experiments. The vault’s isolation didn’t affect the residents. They maintained an orderly, democratic society, and, unlike other vaults, the overseer wasn''t a dictator or a megalomaniac.','available',4,7,7);
INSERT INTO properties_properties (type, size, rooms, price, "yearBuilt", description, status, agent_id, details_id, address_id) VALUES('apartment',130,4,25000000,2009,'As part of the Vault experiment, the armory was overstocked with weapons and ammunition. It was also equipped with a great number of recreational facilities, including a full-sized swimming pool, at the cost of living space.','available',5,8,8);
/*house 5 fallout*/
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/fallout/images/b/b6/Vault_111.png/revision/latest?cb=20150608181823', 5, 'mynd 17');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('http://mmo4ever.com/maps/gfx/screenshots/2015/12/1920/vault-111-recreation-terminal-2.jpg', 5, 'mynd 18');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://pm1.narvii.com/6803/48f19f5be10fc6664c4b1250810954b029911f0av2_hq.jpg', 5, 'mynd 19');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://staticdelivery.nexusmods.com/mods/1151/images/19663-0-1477870285.jpg', 5, 'mynd 20');
/*house 6 fallout */
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/fallout/images/a/a2/Vault95.png/revision/latest?cb=20170520142239', 6, 'mynd 21');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://i.redd.it/rhpzm986v28z.png', 6, 'mynd 22');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://guides.gamepressure.com/fallout4/gfx/word/85799754.jpg', 6, 'mynd 23');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://guides.gamepressure.com/fallout4/gfx/word/85799785.jpg', 6, 'mynd 24');
/* house 7 fallout */
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/fallout/images/3/34/Vault_3.jpg/revision/latest?cb=20110430122718', 7, 'mynd 25');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/fallout/images/f/fd/Vault_3_Cafeteria.jpeg/revision/latest?cb=20120705134333', 7, 'mynd 26');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://gamepedia.cursecdn.com/fallout_gamepedia/4/42/Chinese_Army_Special_Ops_Training_Manual.jpg?version=51ce10c9305b85a317bca8c1e8788e19', 7, 'mynd 27');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/fallout/images/5/53/Recreation_area.jpg/revision/latest?cb=20120325034336', 7, 'mynd 28');
/* house 8 fallout */
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/fallout/images/9/96/Vault_34_exterior.jpg/revision/latest?cb=20121117172538', 8, 'mynd 29');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/fallout/images/6/68/Allamericanlocation.jpg/revision/latest?cb=20150528090553', 8, 'mynd 30');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/fallout/images/6/6f/Overseers_office_vault_34.png/revision/latest?cb=20140629092443', 8, 'mynd 31');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/fallout/images/0/0d/Vault_34_door.png/revision/latest?cb=20140629092422', 8, 'mynd 32');
/*bioshock*/
INSERT INTO properties_propertiesaddress("streetName","houseNumber","zipCode",city,country) VALUES('Montgomery Residence',78,102,'Columbia','Bioshock');
INSERT INTO properties_propertiesaddress("streetName","houseNumber","zipCode",city,country) VALUES('Comstock House',36,102,'Columbia','Bioshock');
INSERT INTO properties_propertiesaddress("streetName","houseNumber","zipCode",city,country) VALUES('Hand of the Prophet',12,102,'Columbia','Bioshock');
INSERT INTO properties_propertiesaddress("streetName","houseNumber","zipCode",city,country) VALUES('Lansdowne Residence',86,102,'Columbia','Bioshock');
INSERT INTO properties_propertiesdetails(garden,garage,pets,accessibility) VALUES(false,false,true,true);
INSERT INTO properties_propertiesdetails(garden,garage,pets,accessibility) VALUES(false,true,true,false);
INSERT INTO properties_propertiesdetails(garden,garage,pets,accessibility) VALUES(true,false,true,false);
INSERT INTO properties_propertiesdetails(garden,garage,pets,accessibility) VALUES(false,false,false,false);
INSERT INTO properties_properties (type, size, rooms, price, "yearBuilt", description, status, agent_id, details_id, address_id) VALUES('apartment',109,4,25000000,1994,'The Montgomery Residence is an apartment located on the eighth floor of a thirteen-story building in Columbia, set on Constitution Square in the Comstock Center Rooftops.','available',7,9,9);
INSERT INTO properties_properties (type, size, rooms, price, "yearBuilt", description, status, agent_id, details_id, address_id) VALUES('house',354,8,31000000,1997,'Comstock House is the executive estate in Columbia. Comstock established the residence as his principal workplace and central headquarters of the Founders.','available',8,10,10);
INSERT INTO properties_properties (type, size, rooms, price, "yearBuilt", description, status, agent_id, details_id, address_id) VALUES('house',124,3,17000000,1998,'The Hand of the Prophet is divided into three main decks, plus a surface deck and a bridge. The first deck is the Hangar Deck, primarily used to accommodate the ship''s crew and the multiple gunships that can dock on the vessel to transport cargo and personnel.','available',9,11,11);
INSERT INTO properties_properties (type, size, rooms, price, "yearBuilt", description, status, agent_id, details_id, address_id) VALUES('apartment',96,2,14000000,1999,'The Lansdowne Residence is the penthouse apartment of a residential building, found amongst the Comstock Center Rooftops of Columbia. .','available',8,12,12);
/* bioshock */
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/bioshock/images/4/47/BioI_Montgomery_Residence_Exterior_Balcony.png/revision/latest?cb=20171127211345', 9, 'mynd 34');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/bioshock/images/9/97/BioI_CCR_Montgomery_Residence_Dining_Room.jpg/revision/latest?cb=20180331233157', 9, 'mynd 35');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/bioshock/images/0/08/BioI_CCR_Montgomery_Residence_Balcony.jpg/revision/latest?cb=20180331233127', 9, 'mynd 36');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/bioshock/images/7/79/BioI_CCR_Montgomery_Residence_Exterior_Constitution_Square.jpg/revision/latest?cb=20180331233222', 9, 'mynd 37');
/* bioshock*/
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/bioshock/images/9/90/Comstock_House_Concept_Art.jpg/revision/latest?cb=20160506211724', 10, 'mynd 38');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/bioshock/images/4/48/Comstock_House_Warden%27s_office.png/revision/latest?cb=20150831182546', 10, 'mynd 39');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/bioshock/images/7/7a/Back21912.jpg/revision/latest?cb=20180219222405', 10, 'mynd 40');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/bioshock/images/3/33/BioI_Comstock_House_Where_We_Learn_Classroom.png/revision/latest?cb=20171214103557', 10, 'mynd 41');
/* bioshock */
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/bioshock/images/b/ba/Hand_Of_The_Prophet_Main_Deck.png/revision/latest?cb=20170208134432', 11, 'mynd 42');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/bioshock/images/5/56/BioI_Hand_of_the_Prophet_Deck_1_Barracks.jpg/revision/latest?cb=20190503214937', 11, 'mynd 43');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/bioshock/images/6/61/BioI_Hand_of_the_Prophet_Deck_1_Galley.jpg/revision/latest?cb=20190503214946', 11, 'mynd 44');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/bioshock/images/7/78/9585704947_dfbce7037d_c.jpg/revision/latest?cb=20131107021822', 11, 'mynd 45');
/* bioshock */
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/bioshock/images/d/de/BioI_CCR_Lansdowne_Residence_Top_Floor_Balcony.jpg/revision/latest?cb=20180611180258', 12, 'mynd 46');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/bioshock/images/d/d8/CCR-Lansdowne.png/revision/latest?cb=20130520072700', 12, 'mynd 47');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/bioshock/images/9/96/BioI_CCR_Lansdowne_Residence_Middle_Floor_Child%27s_Bedroom.jpg/revision/latest?cb=20180611175529', 12, 'mynd 48');
INSERT INTO properties_propertiesimages (link, property_id, text) VALUES('https://vignette.wikia.nocookie.net/bioshock/images/d/db/BioI_CCR_Lansdowne_Residence_Bottom_Floor_Study.jpg/revision/latest?cb=20180611180125', 12, 'mynd 49');
