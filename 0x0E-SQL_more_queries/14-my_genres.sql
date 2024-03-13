-- Use the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT g.id, g.name
FROM tv_genres AS g IN(
	SELECT s
	FROM tv_shows AS s
	WHERE s.title = Dexter
)
ORDER BY g.name;
