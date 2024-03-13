-- Lists all cities contained in the dataase hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM hbtn_0d_usa.states.cities INNER JOIN hbtn_0d_usa.states ORDER BY cities.id ASC;
