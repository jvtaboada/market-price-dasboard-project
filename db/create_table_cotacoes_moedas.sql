-- public.cotacoes_moedas definition
-- Drop table

-- DROP TABLE public.cotacoes_moedas;
CREATE TABLE public.cotacoes_moedas (
	id serial4 NOT NULL,
	moeda bpchar(3) NOT NULL,
	cotacaoCompra numeric(18, 6) NOT NULL,
	horaCotacaoFechamento timestamptz NOT NULL,
	insert_at timestamptz DEFAULT now() NOT NULL,
	CONSTRAINT cotacoes_moedas_pkey PRIMARY KEY (id)
);

-- Permissions
ALTER TABLE public.cotacoes_moedas OWNER TO postgres;
GRANT ALL ON TABLE public.cotacoes_moedas TO postgres;