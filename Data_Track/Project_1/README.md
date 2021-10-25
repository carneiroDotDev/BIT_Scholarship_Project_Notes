# Project 1 Sakila Movie Database
This repository creates details on how to go about the sakila database and answers all the rubric questions

**The project broadens our knowledge of:**
* windows functions and subqueries
* Writing a [neat](https://codebeautify.org/sqlformatter) readable query 
* Visualization skills
* Presentation skills

**To pass this project:**
You should be able to
1. Write at least one query that contains windows function *eg*
    * (NTILE) OVER (PARTITION OVER (name of column you want to partition), ORDER BY (name of column you want to order by))
2. Write subqueries *eg*
    * SELECT *
      FROM(
          SELECT column1_name, SUM(column2_name)
          FROM table1
          GROUP BY column1_name
          ORDER BY SUM(column2_name)
      )sub1
3. Must contain aggregate functions e.g
    * SELECT column1, COUNT(column3)
        FROM table1
        WHERE column1 >= n
        GROUP BY column1
        ORDER BY COUNT(column2) DESC
4. Be sure to test all your codes to make sure they run
5. Your visualization should be a graphical representation of your query results

