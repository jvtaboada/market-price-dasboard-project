create table public.cotacoes(
	id serial primary key,
	ativo character varying(10)	not null,
	preco numeric(18,6) not null,
	moeda char(3) not null,
	horario_coleta timestamptz not null,
	insert_at timestamptz not null default NOW()
);