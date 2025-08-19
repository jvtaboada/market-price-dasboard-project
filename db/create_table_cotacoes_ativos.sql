-- public.cotacoes_ativos definition
-- Drop table

-- DROP TABLE public.cotacoes_ativos;
CREATE TABLE public.cotacoes_ativos (
	id serial4 NOT NULL,
	ativo varchar(10) NOT NULL,
	preco numeric(18, 6) NOT NULL,
	moeda bpchar(3) NOT NULL,
	hora_coleta timestamptz NOT NULL,
	insert_at timestamptz DEFAULT now() NOT NULL,
	CONSTRAINT cotacoes_pkey PRIMARY KEY (id)
);

-- Permissions
ALTER TABLE public.cotacoes_ativos OWNER TO postgres;
GRANT ALL ON TABLE public.cotacoes_ativos TO postgres;