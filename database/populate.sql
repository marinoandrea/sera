begin transaction;

insert into user_group (name)
values ('radio'), ('op'), ('farmer'), ('union'), ('staff');

insert into seed_category (main_category, subcategory)
values 
    ('fonio', 'Pon de Bore'),
    ('fonio', 'Niatia'),
    ('fonio', 'Banco Konkountre'),
    ('fonio', 'other'),
    ('mais', 'Sotubaka'),
    ('mais', 'Nieleni'),
    ('mais', 'Dembaniouma'),
    ('mais', 'other'),   
    ('rice', 'Gambiaka'),
    ('rice', 'Shwetassoke'),
    ('rice', 'Nerica'),
    ('rice', 'other'),   
    ('sorgho', 'Toroba'),
    ('sorgho', 'Bobodje'),
    ('sorgho', 'Tieblen'),
    ('sorgho', 'other');

end transaction;
