use 4linux;

CREATE TABLE pessoa(
    id_pessoa int not null auto_increment,
    nome_pessoa varchar(50) not null,
    nacionalidade_pessoa varchar(20) not null,
    idade_pessoa int not null,
    PRIMARY KEY (id_pessoa)
);

