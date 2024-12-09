-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema telecom_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema telecom_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `telecom_db` DEFAULT CHARACTER SET utf8 ;
USE `telecom_db` ;

-- -----------------------------------------------------
-- Table `telecom_db`.`grupos_economicos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `telecom_db`.`grupos_economicos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `telecom_db`.`empresas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `telecom_db`.`empresas` (
  `cnpj` VARCHAR(14) NOT NULL,
  `nome` VARCHAR(255) NOT NULL,
  `porte` VARCHAR(50) NOT NULL,
  `grupos_economicos_id` INT NOT NULL,
  PRIMARY KEY (`cnpj`, `grupos_economicos_id`),
  INDEX `fk_empresas_grupos_economicos_idx` (`grupos_economicos_id` ASC) VISIBLE,
  CONSTRAINT `fk_empresas_grupos_economicos`
    FOREIGN KEY (`grupos_economicos_id`)
    REFERENCES `telecom_db`.`grupos_economicos` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `telecom_db`.`cidades`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `telecom_db`.`cidades` (
  `codigo_ibge` INT NOT NULL,
  `nome` VARCHAR(50) NOT NULL,
  `uf` CHAR(2) NOT NULL,
  PRIMARY KEY (`codigo_ibge`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `telecom_db`.`operacoes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `telecom_db`.`operacoes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cidades_codigo_ibge` INT NOT NULL,
  `empresas_cnpj` VARCHAR(14) NOT NULL,
  `faixa_velocidade` VARCHAR(50) NULL,
  `velocidade` DECIMAL(10,2) NULL,
  `tecnologia` VARCHAR(50) NULL,
  `meio_acesso` VARCHAR(50) NULL,
  `tipo_pessoa` VARCHAR(50) NULL,
  `tipo_produto` VARCHAR(50) NULL,
  `acessos` INT NULL,
  PRIMARY KEY (`id`, `cidades_codigo_ibge`, `empresas_cnpj`),
  INDEX `fk_operacoes_empresas1_idx` (`empresas_cnpj` ASC) VISIBLE,
  INDEX `fk_operacoes_cidades1_idx` (`cidades_codigo_ibge` ASC) VISIBLE,
  CONSTRAINT `fk_operacoes_empresas1`
    FOREIGN KEY (`empresas_cnpj`)
    REFERENCES `telecom_db`.`empresas` (`cnpj`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_operacoes_cidades1`
    FOREIGN KEY (`cidades_codigo_ibge`)
    REFERENCES `telecom_db`.`cidades` (`codigo_ibge`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Create Views`
-- -----------------------------------------------------
CREATE VIEW empresas_porte AS
SELECT 
    cnpj,
    porte
FROM empresas;

CREATE VIEW empresas_porte_grande AS
SELECT 
    cnpj,
    porte
FROM empresas
WHERE UPPER(porte) = 'GRANDE';


CREATE VIEW empresas_porte_media AS
SELECT 
    cnpj,
    porte
FROM empresas
WHERE UPPER(porte) = 'MEDIA';


CREATE VIEW empresas_porte_pequena AS
SELECT 
    cnpj,
    porte
FROM empresas
WHERE UPPER(porte) = 'PEQUENA';

CREATE VIEW velocidade_maior_50 AS
SELECT
    id,
    cidades_codigo_ibge,
    empresas_cnpj,
    velocidade
FROM operacoes
WHERE velocidade > 50.00;

CREATE VIEW velocidade_menor_50 AS
SELECT
    id,
    cidades_codigo_ibge,
    empresas_cnpj,
    velocidade
FROM operacoes
WHERE velocidade < 50.00;

-- -----------------------------------------------------
-- Table `Create Triggers`
-- -----------------------------------------------------

DELIMITER //

CREATE TRIGGER trg_validar_porte
BEFORE INSERT ON empresas
FOR EACH ROW
BEGIN
    IF NEW.porte NOT IN('Grande', 'Media', 'Pequena') THEN
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Porte inválido. Insira um porte válido!';
    END IF;
END;


-- OPERACAO
-- OK
CREATE TRIGGER tgr_validar_tipo_pessoa
BEFORE INSERT ON operacoes
FOR EACH ROW
BEGIN
    IF NEW.tipo_pessoa NOT IN('Fisica', 'Juridica') THEN
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Tipo de pessoa inválido. Insira um tipo válido!';
    END IF;
END;


CREATE TRIGGER tgr_validar_meio_acesso
BEFORE INSERT ON operacoes
FOR EACH ROW
BEGIN
    IF NEW.meio_acesso NOT IN('Fibra Otica', 'Cabo','Satelite', '5G', '4G', 'ADSL') THEN
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Meio de acesso inválido. Insira um tipo válido!';
    END IF;
END;

-- OK
CREATE TRIGGER tgr_validar_tipo_produto
BEFORE INSERT ON operacoes
FOR EACH ROW
BEGIN
    IF NEW.tipo_produto NOT IN(
        'Plano de Internet', 'Modem', 'Roteador', 'Plano Corporativo', 'Plano Residencial'
    ) THEN
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Tipo de produto inválido. Insira um tipo válido!';
    END IF;
END;

//


DELIMITER ;





SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
