Select * from gamerraterapi_category;
Select * from gamerraterapi_game;
SELECT * FROM auth_user;
SELECT * FROM authtoken_token;
SELECT * FROM gamerraterapi_category;
SELECT * FROM gamerraterapi_gamecategory;
SELECT * FROM gamerraterapi_entry;
SELECT * FROM gamerraterapi_player;
SELECT * FROM gamerraterapi_picture;

-- How many games don't have pictures?
with picturecount as (Select g.title game, count(p.id) pictures
From gamerraterapi_game g
JOIN gamerraterapi_picture p on g.id = p.game_id
GROUP BY game)
select count(game) GamesNoPics
from picturecount
where pictures = 0;

-- By count, who are the top three game reviewers?

with UserReviews as
(select u.first_name || " " || u.last_name as Player,
count(r.id) Reviews
from gamerraterapi_player p
join gamerraterapi_review r on r.player_id = p.id
join auth_user u on u.id = p.user_id)
Select Player, max(Reviews) NumReviews
from UserReviews;