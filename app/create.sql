
/*用户表*/
drop table if exists users;
    create table users(                                     
        student_number varchar(15) primary key not null,    /*学号*/
        name varchar(20) not null,                          /*姓名*/
        password varchar(20) not null                       /*密码*/
    );

INSERT INTO users values ('2014111526', 'LIKE', '123456');
INSERT INTO users values ('2014111530', 'DGVY', '654321');

/*物品表*/