--lists all shows contained in the database hbtn_0d_tvshows.`
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows AS s LEFT JOIN tv_show_genres AS g
ON s.id = g.show_id
ORDER BY s.title ASC, g.genre_id ASC;
