-- kullanıcılar

-- ALTER SEQUENCE kullanici_id_seq RESTART WITH 1;
-- SELECT * FROM kullanicilar;
-- DELETE FROM kullanicilar;

INSERT INTO kullanicilar VALUES ('Ford', 'Prefect', nextval('kullanici_id_seq'), 'fordprefect@hitchhiker.com', '12345678', '1970-01-01', 0, 'Kiraci');
INSERT INTO kullanicilar VALUES ('Arthur', 'Dent', nextval('kullanici_id_seq'), 'arthurdent@earth.com', '12345678', '1977-06-24', 0, 'Kiraci');
INSERT INTO kullanicilar VALUES ('Zaphod', 'Beeblebrox', nextval('kullanici_id_seq'), 'zaphodbeeblebrox@galaxy.com', '12345678', '1965-11-29', 0, 'Kiraci');
INSERT INTO kullanicilar VALUES ('Tricia', 'McMillan', nextval('kullanici_id_seq'), 'trillian@earth.com', '12345678', '1978-02-10', 0, 'Kiraci');
INSERT INTO kullanicilar VALUES ('Seray', 'Çelik', nextval('kullanici_id_seq'), 'seraycelik@gardenhub.com', '12345678', '2000-01-01', 0, 'Kiraci');
INSERT INTO kullanicilar VALUES ('İclal', 'Ertürk', nextval('kullanici_id_seq'), 'iclalerturk@gardenhub.com', '12345678', '2000-01-01', 0, 'Kiraci');
INSERT INTO kullanicilar VALUES ('Şeyma', 'Başaran', nextval('kullanici_id_seq'), 'seymabasaran@gardenhub.com', '12345678', '2000-01-01', 0, 'Kiraci');
INSERT INTO kullanicilar VALUES ('Luke', 'Skywalker', nextval('kullanici_id_seq'), 'lukeskywalker@galaxy.com', '12345678', '1960-05-04', 0, 'Kiraci');
INSERT INTO kullanicilar VALUES ('Leia', 'Organa', nextval('kullanici_id_seq'), 'leiaorgana@galaxy.com', '12345678', '1960-05-04', 0, 'Kiraci');
INSERT INTO kullanicilar VALUES ('Paul', 'Atreides', nextval('kullanici_id_seq'), 'paulatreides@arrakis.com', '12345678', '1980-07-08', 0, 'Kiraci');


-- yonetici

INSERT INTO yonetici VALUES ('admin@gardenhub.com', 'admin');
-- urunler
INSERT INTO urunler VALUES (nextval('urun_id_seq'),'Havuç', 2, 40,2);
INSERT INTO urunler VALUES (nextval('urun_id_seq'),'Maydaoz', 3, 50,2);
INSERT INTO urunler VALUES (nextval('urun_id_seq'),'Marul', 5, 60,2);
INSERT INTO urunler VALUES (nextval('urun_id_seq'),'Nane', 6, 60,2);
INSERT INTO urunler VALUES (nextval('urun_id_seq'),'Patates', 4, 40,2);
INSERT INTO urunler VALUES (nextval('urun_id_seq'),'Biber', 3, 80,2);
INSERT INTO urunler VALUES (nextval('urun_id_seq'),'Fasulye', 8, 70,2);
INSERT INTO urunler VALUES (nextval('urun_id_seq'),'Salatalık', 10, 30,2);
INSERT INTO urunler VALUES (nextval('urun_id_seq'),'Domates', 5, 55,2);
INSERT INTO urunler VALUES (nextval('urun_id_seq'),'Üzüm', 4, 50,2);
--alter table urunler add column urun_id int;
-- Ekipman

INSERT INTO Ekipman VALUES (nextval('ekipman_id_seq'), 'Kürek', '12', 40);
INSERT INTO Ekipman VALUES (nextval('ekipman_id_seq'), 'Çapa', '7', 50);
INSERT INTO Ekipman VALUES (nextval('ekipman_id_seq'), 'Budama Makası', '8', 60);
INSERT INTO Ekipman VALUES (nextval('ekipman_id_seq'), 'Balta', '3', 60);
INSERT INTO Ekipman VALUES (nextval('ekipman_id_seq'), 'Tırmık', '5', 40);
INSERT INTO Ekipman VALUES (nextval('ekipman_id_seq'), 'El Arabası', '3', 80);
INSERT INTO Ekipman VALUES (nextval('ekipman_id_seq'), 'Çim Makası', '6', 70);
INSERT INTO Ekipman VALUES (nextval('ekipman_id_seq'), 'Eldiven', '15', 30);
INSERT INTO Ekipman VALUES (nextval('ekipman_id_seq'), 'Bahçe Hortumu', '16', 55);
INSERT INTO Ekipman VALUES (nextval('ekipman_id_seq'), 'Kazma', '4', 50);


-- Bahceler
SELECT * FROM Bahceler;
INSERT INTO Bahceler VALUES (1, 10, '1/1', 'Humuslu', 'Bos', '800');
INSERT INTO Bahceler VALUES (2, 10, '1/2', 'Tınlı', 'Bos', '700');
INSERT INTO Bahceler VALUES (3, 10, '1/3', 'Kireçli', 'Bos', '600');
INSERT INTO Bahceler VALUES (4, 10, '1/4', 'Killi', 'Bos', '600');
INSERT INTO Bahceler VALUES (5, 10, '2/1', 'Torf', 'Bos', '600');
INSERT INTO Bahceler VALUES (6, 10, '2/2', 'Humuslu', 'Bos', '800');
INSERT INTO Bahceler VALUES (7, 10, '2/3', 'Tınlı', 'Bos', '700');
INSERT INTO Bahceler VALUES (8, 10, '2/4', 'Kireçli', 'Bos', '600');
INSERT INTO Bahceler VALUES (9, 10, '3/1', 'Killi', 'Bos', '600');
INSERT INTO Bahceler VALUES (10, 10, '3/2', 'Torf', 'Bos', '600');
INSERT INTO Bahceler VALUES (11, 10, '3/3', 'Humuslu', 'Bos', '800');
INSERT INTO Bahceler VALUES (12, 10, '3/4', 'Humuslu', 'Bos', '800');
INSERT INTO Bahceler VALUES (13, 10, '4/1', 'Tınlı', 'Bos', '700');
INSERT INTO Bahceler VALUES (14, 10, '4/2', 'Kireçli', 'Bos', '600');
INSERT INTO Bahceler VALUES (15, 10, '4/3', 'Killi', 'Bos', '600');
INSERT INTO Bahceler VALUES (16, 10, '4/4', 'Torf', 'Bos', '600');


-- Kiralamalar

-- EkipmanTalep