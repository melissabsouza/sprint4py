CREATE TABLE TB_RDC_CADASTRO(
    id NUMBER PRIMARY KEY,
    cnpj number,
    nm_cadastro varchar(200),
    sobrenome_cadastro varchar(200),
    cargo_cadastro varchar(200),
    email_cadastro varchar(200),
    telefone_cadastro number,
    nm_empresa_cadastro varchar(200),
    tam_empresa varchar(200),
    pais_cadastro varchar(200),
    idioma_cadastro varchar(200)
);

CREATE SEQUENCE cadastro_seq
START WITH 1
INCREMENT BY 1;

CREATE OR REPLACE TRIGGER trg_cadastro_id
BEFORE INSERT ON TB_RDC_CADASTRO
FOR EACH ROW
BEGIN
    :new.id := cadastro_seq.NEXTVAL;
END;
/


CREATE TABLE T_RDC_LOGIN(
    id_login NUMBER PRIMARY KEY,
    usuario_login VARCHAR2(200),
    senha_login VARCHAR2(200),
    status_login CHAR(2) CHECK(status_login in ('A', 'I')),
    id_cadastro NUMBER,
    CONSTRAINT fk_login_cadastro FOREIGN KEY (id_cadastro) REFERENCES T_RDC_CADASTRO(id_cadastro)
);

CREATE TABLE T_RDC_INFO_EMP_CLIENTE(
    id_info_emp_cliente NUMBER PRIMARY KEY,
    rua_info_emp VARCHAR2(200),
    bairro_info_emp VARCHAR2(200),
    cep_info_emp NUMBER,
    num_info_emp NUMBER,
    ramo_info_emp VARCHAR2(200),
    id_cadastro NUMBER,
    CONSTRAINT fk_info_cadastro FOREIGN KEY (id_cadastro) REFERENCES T_RDC_CADASTRO(id_cadastro)
);


CREATE TABLE T_RDC_TELEFONE(
    id_telefone NUMBER PRIMARY KEY,
    fixo_telefone NUMBER,
    celular_telefone NUMBER,
    ddd_telefone NUMBER,
    ddi_telefone NUMBER,
    id_info_emp_cliente NUMBER,
    CONSTRAINT fk_telefone_info FOREIGN KEY (id_info_emp_cliente) REFERENCES T_RDC_INFO_EMP_CLIENTE(id_info_emp_cliente)
);