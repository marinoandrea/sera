begin transaction;

create table user_group (
    name text not null,
    primary key (name)
);

create table user_account (

    id text not null,
    created_at bigint not null default (extract(epoch from CURRENT_TIMESTAMP) * 1000)::bigint,
    updated_at bigint not null default (extract(epoch from CURRENT_TIMESTAMP) * 1000)::bigint,

    name text,
    email text,
    password text,
    phone_number text,
    user_group text not null,
    is_admin boolean not null default false,

    primary key (id),
    unique (email),
    unique (phone_number),
    foreign key (user_group) references user_group(name)

);

create table seed_category (
    main_category text not null,
    subcategory text not null,
    primary key (main_category, subcategory)
);

create table offering (

    id text not null,
    created_at bigint not null default (extract(epoch from CURRENT_TIMESTAMP) * 1000)::bigint,
    updated_at bigint not null default (extract(epoch from CURRENT_TIMESTAMP) * 1000)::bigint,

    user_account_id text not null,
    category text not null,
    subcategory text not null,
    quantity_kg float not null,
    price_per_kg_cfa_cents integer not null,

    primary key (id),
    foreign key (user_account_id) references user_account(id),
    foreign key (category, subcategory) references seed_category(main_category, subcategory),
    unique (user_account_id, category, subcategory, created_at)

);

create table offering_audio (

    id text not null,
    created_at bigint not null default (extract(epoch from CURRENT_TIMESTAMP) * 1000)::bigint,
    updated_at bigint not null default (extract(epoch from CURRENT_TIMESTAMP) * 1000)::bigint,

    offering_id text not null,
    lang char(2) not null,
    path text not null,

    primary key (id),
    foreign key (offering_id) references offering(id)

);

end transaction;
