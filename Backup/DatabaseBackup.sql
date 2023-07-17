BEGIN TRANSACTION;
CREATE TABLE clientes(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER, 
        cpf VARCHAR(11) NOT NULL
    , cidade VARCHAR(30));
INSERT INTO "clientes" VALUES(1,'Joao',26,'123.456.789-01',NULL);
INSERT INTO "clientes" VALUES(2,'Camila',26,'552.456.852-96',NULL);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('clientes',3);
COMMIT;
