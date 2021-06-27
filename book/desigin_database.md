book
1. id
1. book_name
2. author
3. description
4. book_cover
5. create_time
7. update_time
8. is_valid

CREATE TABLE book (  
    id int NOT NULL primary key AUTO_INCREMENT,
    book_name VARCHAR  (100),
    author    VARCHAR (100),
    description VARCHAR (2000), 
    book_cover VARCHAR (100),
    create_time DATETIME ,
    update_time DATETIME ,
    is_valid tinyint
) default charset=utf8 ;


chapter
1. id    
2. content
3. book_id
3. created_time
4. update_time
5. is_vaild
chapter 详情不写了
不见了 
