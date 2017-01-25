
/*用户表*/
drop table if exists users;
    create table users(                                     
        student_number varchar(15) primary key not null,    /*学号*/
        name varchar(20) not null,                          /*姓名*/
        password varchar(20) not null                       /*密码*/
    );

/*物品表*/