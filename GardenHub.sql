create sequence kullanici_id_seq
minvalue 1
increment by 1

CREATE TABLE kullanicilar (
    isim VARCHAR(20) NOT NULL,
    soyisim VARCHAR(20) NOT NULL,
    kullanici_id INT NOT NULL PRIMARY KEY,
    mail VARCHAR(70) NOT NULL,
    sifre VARCHAR(20) NOT NULL,
    bdate DATE,
    butce numeric(10,2) DEFAULT 0,
    user_type VARCHAR(50) CHECK (user_type IN ('Kiraci', 'Kullanici')),
    CONSTRAINT yas_sinir CHECK (AGE(CURRENT_DATE, bdate) >= INTERVAL '18 years')
);

create table yonetici(
	mail varchar(70),
	sifre varchar(20)
);

create sequence urun_id_seq
minvalue 1000
increment by 1

create table urunler(
	urun_id int not null primary key,
	urun_adi varchar(20) not null,
	kg int,
	fiyat int NOT NULL CHECK (Fiyat > 0),
	sahip_id int references kullanicilar(kullanici_id)	
);

create sequence ekipman_id_seq
minvalue 10000
increment by 1

CREATE TABLE Ekipman (
	ekipman_id int not null primary key,
	ekipman_adi varchar(20) not null,
	ekipman_sayisi int not null,
    fiyat NUMERIC(10,2) NOT NULL CHECK (fiyat > 0)
);

-- 2. Bahçeler Tablosu
CREATE TABLE Bahceler (
	bahce_id int NOT NULL PRIMARY KEY,
	alan NUMERIC(5,2) NOT NULL,
	konum varchar(20),
	toprak_tipi varchar(20),
    durum VARCHAR(20) NOT NULL CHECK (Durum IN ('Bos', 'Kiralanmis')),
    fiyat NUMERIC(10,2) NOT NULL CHECK (Fiyat > 0)
);

create sequence kiralama_id_seq
minvalue 1000
increment by 1

-- 3. Kiralamalar Tablosu
CREATE TABLE Kiralamalar (
    kiralama_id int PRIMARY KEY,
    kullanici_id INT,
    bahce_id INT REFERENCES Bahceler(bahce_id),
    baslangic_tarihi DATE NOT NULL,
	constraint kullanicilar_kullanici_id_fkey foreign key (kullanici_id) 
	references kullanicilar(kullanici_id) on delete cascade
);
select * from kiralamalar
drop trigger trigger_update_bahce_durum on kiralamalar
drop function update_bahce_durum_on_kiralama
drop table kiralamalar

CREATE TRIGGER trigger_update_bahce_durum
AFTER INSERT ON Kiralamalar
FOR EACH ROW
EXECUTE FUNCTION update_bahce_durum_on_kiralama();

CREATE OR REPLACE FUNCTION update_bahce_durum_on_kiralama()
RETURNS TRIGGER AS $$
BEGIN
    -- Kiralama eklenen bahçenin durumunu "Kiralanmış" olarak güncelle
    UPDATE bahceler
    SET durum = 'Kiralanmis'
    WHERE bahce_id = NEW.bahce_id;
	--kullanicinin türünü kiracaı yap
	UPDATE kullanicilar
	set user_type = 'Kiraci'
	where kullanici_id=NEW.kullanici_id;
	
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_sifirla_bahce_durum
AFTER DELETE ON Kiralamalar
FOR EACH ROW
EXECUTE FUNCTION sifirla_bahce_durum_on_bahceler();

CREATE OR REPLACE FUNCTION sifirla_bahce_durum_on_bahceler()
RETURNS TRIGGER AS $$
BEGIN
    -- Kiralama eklenen bahçenin durumunu "Kiralanmış" olarak güncelle
    UPDATE bahceler
    SET durum = 'Bos'
    WHERE bahce_id = NEW.bahce_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TABLE EkipmanTalep (
    talep_id int PRIMARY KEY,
    kullanici_id INT REFERENCES Kullanicilar(kullanici_id),
    ekipman_id INT REFERENCES Ekipman(ekipman_id),
    miktar INT CHECK (Miktar > 0),
    talep_tarihi DATE DEFAULT CURRENT_DATE
);

CREATE OR REPLACE FUNCTION kullanici_mail_var_mi(email TEXT)
RETURNS BOOLEAN AS $$
DECLARE
    mail_var BOOLEAN;
BEGIN
    -- E-posta adresinin var olup olmadığını kontrol et
    SELECT EXISTS (SELECT 1 FROM kullanicilar WHERE mail = email) INTO mail_var;

    RETURN mail_var;
END;
$$ LANGUAGE plpgsql;






