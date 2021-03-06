PGDMP                         v            library    9.5.13    9.5.13 G    	           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            	           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            	           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            	           1262    26260    library    DATABASE     m   CREATE DATABASE library WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_IN' LC_CTYPE = 'en_IN';
    DROP DATABASE library;
             srmehta    false            	            2615    26261    library    SCHEMA        CREATE SCHEMA library;
    DROP SCHEMA library;
             srmehta    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            	           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    7            	           0    0    SCHEMA public    ACL     �   REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;
                  postgres    false    7                        3079    12393    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false            	           0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    1                        3079    26262    citext 	   EXTENSION     :   CREATE EXTENSION IF NOT EXISTS citext WITH SCHEMA public;
    DROP EXTENSION citext;
                  false    7            	           0    0    EXTENSION citext    COMMENT     S   COMMENT ON EXTENSION citext IS 'data type for case-insensitive character strings';
                       false    2            [           1247    26346    email    DOMAIN     �   CREATE DOMAIN public.email AS public.citext
	CONSTRAINT email_check CHECK ((VALUE OPERATOR(public.~) '^[a-zA-Z0-9.!#$%&''*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zAZ0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'::public.citext));
    DROP DOMAIN public.email;
       public       srmehta    false    2    2    2    7    7    2    7    2    7    2    7    2    2    7    7    2    7    2    7    2    7    7    2    7    2    2    7    7    2    7    2    7    2    7    2    2    7    7    2    7    2    7    2    7    2    2    7    7    2    7    2    7    2    7    7    2    2    7    7    2    7    2    7    2    7    2    7    2    7            ]           1247    26348    phone    DOMAIN     �   CREATE DOMAIN public.phone AS public.citext
	CONSTRAINT phone_check CHECK ((VALUE OPERATOR(public.~) '^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'::public.citext));
    DROP DOMAIN public.phone;
       public       srmehta    false    2    2    7    7    2    7    2    7    2    7    2    2    2    7    7    2    7    2    7    2    7    2    2    7    7    2    7    2    7    2    7    7    2    7    2    2    7    7    2    7    2    7    2    7    2    2    7    7    2    7    2    7    2    7    2    7    2    7    7    2    2    7    7    2    7    2    7    2    7            �            1259    42810    book    TABLE     �  CREATE TABLE library.book (
    id integer NOT NULL,
    name character varying(50),
    picture character varying(100) DEFAULT 'default-book.jpg'::character varying NOT NULL,
    publication character varying(30) NOT NULL,
    author1 character varying(30) NOT NULL,
    author2 character varying(30),
    quantity smallint NOT NULL,
    year smallint NOT NULL,
    price smallint NOT NULL,
    active boolean DEFAULT true,
    cid smallint
);
    DROP TABLE library.book;
       library         srmehta    false    9            �            1259    42808    book_id_seq    SEQUENCE     u   CREATE SEQUENCE library.book_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE library.book_id_seq;
       library       srmehta    false    192    9            	           0    0    book_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE library.book_id_seq OWNED BY library.book.id;
            library       srmehta    false    191            �            1259    50999    book_occupied    TABLE     �  CREATE TABLE library.book_occupied (
    id integer NOT NULL,
    bid smallint NOT NULL,
    sid smallint NOT NULL,
    returned boolean DEFAULT false NOT NULL,
    purchased_date timestamp without time zone DEFAULT now() NOT NULL,
    return_date timestamp without time zone DEFAULT (now() + '15 days'::interval),
    auto_renew boolean DEFAULT false NOT NULL,
    active boolean DEFAULT true NOT NULL
);
 "   DROP TABLE library.book_occupied;
       library         srmehta    false    9            �            1259    50997    book_occuppied_id_seq    SEQUENCE        CREATE SEQUENCE library.book_occuppied_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE library.book_occuppied_id_seq;
       library       srmehta    false    194    9            	           0    0    book_occuppied_id_seq    SEQUENCE OWNED BY     P   ALTER SEQUENCE library.book_occuppied_id_seq OWNED BY library.book_occupied.id;
            library       srmehta    false    193            �            1259    34454    chat    TABLE     �   CREATE TABLE library.chat (
    id integer NOT NULL,
    name character varying(10) NOT NULL,
    message character varying(100) NOT NULL,
    date date,
    "time" time without time zone,
    active boolean DEFAULT false
);
    DROP TABLE library.chat;
       library         srmehta    false    9            �            1259    34452    chat_id_seq    SEQUENCE     u   CREATE SEQUENCE library.chat_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE library.chat_id_seq;
       library       srmehta    false    9    188            	           0    0    chat_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE library.chat_id_seq OWNED BY library.chat.id;
            library       srmehta    false    187            �            1259    51022    course    TABLE     �   CREATE TABLE library.course (
    id integer NOT NULL,
    cname character varying(50),
    branch character varying(50) NOT NULL,
    total_books smallint DEFAULT 0 NOT NULL,
    active boolean DEFAULT true
);
    DROP TABLE library.course;
       library         srmehta    false    9            �            1259    51020    course_id_seq    SEQUENCE     w   CREATE SEQUENCE library.course_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE library.course_id_seq;
       library       srmehta    false    9    196            	           0    0    course_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE library.course_id_seq OWNED BY library.course.id;
            library       srmehta    false    195            �            1259    26380    otp    TABLE       CREATE TABLE library.otp (
    id integer NOT NULL,
    user_id integer NOT NULL,
    otp character varying(6) NOT NULL,
    expires_on timestamp without time zone DEFAULT (now() + '00:05:00'::interval) NOT NULL,
    active boolean DEFAULT true NOT NULL
);
    DROP TABLE library.otp;
       library         srmehta    false    9            �            1259    26378 
   otp_id_seq    SEQUENCE     t   CREATE SEQUENCE library.otp_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE library.otp_id_seq;
       library       srmehta    false    186    9            	           0    0 
   otp_id_seq    SEQUENCE OWNED BY     ;   ALTER SEQUENCE library.otp_id_seq OWNED BY library.otp.id;
            library       srmehta    false    185            �            1259    42720    student    TABLE     �  CREATE TABLE library.student (
    id integer NOT NULL,
    username character varying(20),
    password character varying(20) NOT NULL,
    fname character varying(20) NOT NULL,
    lname character varying(20) NOT NULL,
    email public.email NOT NULL,
    phone public.phone NOT NULL,
    gender boolean NOT NULL,
    dob date NOT NULL,
    address character varying(200) NOT NULL,
    picture character varying(100) DEFAULT 'profile-pic.jpg'::character varying NOT NULL,
    last_login timestamp without time zone DEFAULT now() NOT NULL,
    live boolean DEFAULT false,
    last_otp_id integer DEFAULT 0 NOT NULL,
    register_on timestamp without time zone DEFAULT now() NOT NULL,
    active boolean DEFAULT false
);
    DROP TABLE library.student;
       library         srmehta    false    605    603    9            �            1259    42718    student_id_seq    SEQUENCE     x   CREATE SEQUENCE library.student_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE library.student_id_seq;
       library       srmehta    false    9    190            	           0    0    student_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE library.student_id_seq OWNED BY library.student.id;
            library       srmehta    false    189            �            1259    26352    user    TABLE     f  CREATE TABLE library."user" (
    id integer NOT NULL,
    username character varying(20),
    password character varying(20) NOT NULL,
    email public.email NOT NULL,
    phone public.phone NOT NULL,
    last_login timestamp without time zone NOT NULL,
    live boolean DEFAULT false,
    last_otp_id integer DEFAULT 0,
    active boolean DEFAULT false
);
    DROP TABLE library."user";
       library         srmehta    false    605    603    9            �            1259    26350    user_id_seq    SEQUENCE     u   CREATE SEQUENCE library.user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE library.user_id_seq;
       library       srmehta    false    184    9             	           0    0    user_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE library.user_id_seq OWNED BY library."user".id;
            library       srmehta    false    183            i           2604    42813    id    DEFAULT     d   ALTER TABLE ONLY library.book ALTER COLUMN id SET DEFAULT nextval('library.book_id_seq'::regclass);
 7   ALTER TABLE library.book ALTER COLUMN id DROP DEFAULT;
       library       srmehta    false    192    191    192            l           2604    51002    id    DEFAULT     w   ALTER TABLE ONLY library.book_occupied ALTER COLUMN id SET DEFAULT nextval('library.book_occuppied_id_seq'::regclass);
 @   ALTER TABLE library.book_occupied ALTER COLUMN id DROP DEFAULT;
       library       srmehta    false    193    194    194            `           2604    34457    id    DEFAULT     d   ALTER TABLE ONLY library.chat ALTER COLUMN id SET DEFAULT nextval('library.chat_id_seq'::regclass);
 7   ALTER TABLE library.chat ALTER COLUMN id DROP DEFAULT;
       library       srmehta    false    188    187    188            r           2604    51025    id    DEFAULT     h   ALTER TABLE ONLY library.course ALTER COLUMN id SET DEFAULT nextval('library.course_id_seq'::regclass);
 9   ALTER TABLE library.course ALTER COLUMN id DROP DEFAULT;
       library       srmehta    false    195    196    196            ]           2604    26383    id    DEFAULT     b   ALTER TABLE ONLY library.otp ALTER COLUMN id SET DEFAULT nextval('library.otp_id_seq'::regclass);
 6   ALTER TABLE library.otp ALTER COLUMN id DROP DEFAULT;
       library       srmehta    false    186    185    186            b           2604    42723    id    DEFAULT     j   ALTER TABLE ONLY library.student ALTER COLUMN id SET DEFAULT nextval('library.student_id_seq'::regclass);
 :   ALTER TABLE library.student ALTER COLUMN id DROP DEFAULT;
       library       srmehta    false    190    189    190            Y           2604    26355    id    DEFAULT     f   ALTER TABLE ONLY library."user" ALTER COLUMN id SET DEFAULT nextval('library.user_id_seq'::regclass);
 9   ALTER TABLE library."user" ALTER COLUMN id DROP DEFAULT;
       library       srmehta    false    183    184    184            	          0    42810    book 
   TABLE DATA               u   COPY library.book (id, name, picture, publication, author1, author2, quantity, year, price, active, cid) FROM stdin;
    library       srmehta    false    192   �R       !	           0    0    book_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('library.book_id_seq', 7, true);
            library       srmehta    false    191            	          0    50999    book_occupied 
   TABLE DATA               q   COPY library.book_occupied (id, bid, sid, returned, purchased_date, return_date, auto_renew, active) FROM stdin;
    library       srmehta    false    194   �S       "	           0    0    book_occuppied_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('library.book_occuppied_id_seq', 8, true);
            library       srmehta    false    193            	          0    34454    chat 
   TABLE DATA               H   COPY library.chat (id, name, message, date, "time", active) FROM stdin;
    library       srmehta    false    188   [T       #	           0    0    chat_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('library.chat_id_seq', 1, false);
            library       srmehta    false    187            	          0    51022    course 
   TABLE DATA               I   COPY library.course (id, cname, branch, total_books, active) FROM stdin;
    library       srmehta    false    196   xT       $	           0    0    course_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('library.course_id_seq', 1, true);
            library       srmehta    false    195            	          0    26380    otp 
   TABLE DATA               D   COPY library.otp (id, user_id, otp, expires_on, active) FROM stdin;
    library       srmehta    false    186   �T       %	           0    0 
   otp_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('library.otp_id_seq', 1, true);
            library       srmehta    false    185            		          0    42720    student 
   TABLE DATA               �   COPY library.student (id, username, password, fname, lname, email, phone, gender, dob, address, picture, last_login, live, last_otp_id, register_on, active) FROM stdin;
    library       srmehta    false    190   U       &	           0    0    student_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('library.student_id_seq', 1, true);
            library       srmehta    false    189            	          0    26352    user 
   TABLE DATA               n   COPY library."user" (id, username, password, email, phone, last_login, live, last_otp_id, active) FROM stdin;
    library       srmehta    false    184   �U       '	           0    0    user_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('library.user_id_seq', 1, true);
            library       srmehta    false    183            �           2606    42818    book_name_key 
   CONSTRAINT     N   ALTER TABLE ONLY library.book
    ADD CONSTRAINT book_name_key UNIQUE (name);
 =   ALTER TABLE ONLY library.book DROP CONSTRAINT book_name_key;
       library         srmehta    false    192    192            �           2606    51009    book_occuppied_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY library.book_occupied
    ADD CONSTRAINT book_occuppied_pkey PRIMARY KEY (id);
 L   ALTER TABLE ONLY library.book_occupied DROP CONSTRAINT book_occuppied_pkey;
       library         srmehta    false    194    194            �           2606    42816 	   book_pkey 
   CONSTRAINT     M   ALTER TABLE ONLY library.book
    ADD CONSTRAINT book_pkey PRIMARY KEY (id);
 9   ALTER TABLE ONLY library.book DROP CONSTRAINT book_pkey;
       library         srmehta    false    192    192            ~           2606    34460 	   chat_pkey 
   CONSTRAINT     M   ALTER TABLE ONLY library.chat
    ADD CONSTRAINT chat_pkey PRIMARY KEY (id);
 9   ALTER TABLE ONLY library.chat DROP CONSTRAINT chat_pkey;
       library         srmehta    false    188    188            �           2606    51031    course_cname_key 
   CONSTRAINT     T   ALTER TABLE ONLY library.course
    ADD CONSTRAINT course_cname_key UNIQUE (cname);
 B   ALTER TABLE ONLY library.course DROP CONSTRAINT course_cname_key;
       library         srmehta    false    196    196            �           2606    51029    course_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY library.course
    ADD CONSTRAINT course_pkey PRIMARY KEY (id);
 =   ALTER TABLE ONLY library.course DROP CONSTRAINT course_pkey;
       library         srmehta    false    196    196            |           2606    26387    otp_pkey 
   CONSTRAINT     K   ALTER TABLE ONLY library.otp
    ADD CONSTRAINT otp_pkey PRIMARY KEY (id);
 7   ALTER TABLE ONLY library.otp DROP CONSTRAINT otp_pkey;
       library         srmehta    false    186    186            �           2606    42734    student_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY library.student
    ADD CONSTRAINT student_pkey PRIMARY KEY (id);
 ?   ALTER TABLE ONLY library.student DROP CONSTRAINT student_pkey;
       library         srmehta    false    190    190            �           2606    42736    student_username_key 
   CONSTRAINT     \   ALTER TABLE ONLY library.student
    ADD CONSTRAINT student_username_key UNIQUE (username);
 G   ALTER TABLE ONLY library.student DROP CONSTRAINT student_username_key;
       library         srmehta    false    190    190            v           2606    26367    user_last_otp_id_key 
   CONSTRAINT     ^   ALTER TABLE ONLY library."user"
    ADD CONSTRAINT user_last_otp_id_key UNIQUE (last_otp_id);
 F   ALTER TABLE ONLY library."user" DROP CONSTRAINT user_last_otp_id_key;
       library         srmehta    false    184    184            x           2606    26363 	   user_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY library."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);
 ;   ALTER TABLE ONLY library."user" DROP CONSTRAINT user_pkey;
       library         srmehta    false    184    184            z           2606    26365    user_username_key 
   CONSTRAINT     X   ALTER TABLE ONLY library."user"
    ADD CONSTRAINT user_username_key UNIQUE (username);
 C   ALTER TABLE ONLY library."user" DROP CONSTRAINT user_username_key;
       library         srmehta    false    184    184            �           2606    51010    book_occuppied_bid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY library.book_occupied
    ADD CONSTRAINT book_occuppied_bid_fkey FOREIGN KEY (bid) REFERENCES library.book(id);
 P   ALTER TABLE ONLY library.book_occupied DROP CONSTRAINT book_occuppied_bid_fkey;
       library       srmehta    false    2182    192    194            �           2606    51015    book_occuppied_sid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY library.book_occupied
    ADD CONSTRAINT book_occuppied_sid_fkey FOREIGN KEY (sid) REFERENCES library.student(id);
 P   ALTER TABLE ONLY library.book_occupied DROP CONSTRAINT book_occuppied_sid_fkey;
       library       srmehta    false    2176    190    194            �           2606    26388    otp_user_id_fkey    FK CONSTRAINT     v   ALTER TABLE ONLY library.otp
    ADD CONSTRAINT otp_user_id_fkey FOREIGN KEY (user_id) REFERENCES library."user"(id);
 ?   ALTER TABLE ONLY library.otp DROP CONSTRAINT otp_user_id_fkey;
       library       srmehta    false    184    2168    186            	     x����j�0��~�`'q��1��d���.�a27��9#1-}��Ia�e��t��~�A�[�a�B��X�5J��?��������<�?�[ؤ��T�}/��5��<�!+���p�I��Q�(��8���P���~� GV��l��Fh�����V|��H���H�P>��r��?�b"(�����"�k��S�P����$|R8dؒBXAR#�i��6q��_��x31(��/�%(� �o���dUgn���//fo���J�{�F���u�i����{��K�}      	   �   x�m��� �᳙�Ĳ��Yz��_���Q�_��ⱑob/�E�zG�n��#�p4�
�]Хm�T�EJ�C/6(-$w�z�pI)H�Ay��P���R��B`�i.O�L)X-t�9c2?�3�0@k�Ņ�ΔB�/_�&��7/)�7��>�c�      	      x������ � �      	   I   x�3�tJL�H��/R�OSp�K��KM-��KW�p�s�����K�/�M,���SIM�����O��4�,����� �b      	   5   x�3�4��5vN4�420��50�52U04�20�25�3132�0�,����� ���      		   �   x�E���  ��W�����E��ܝ]H�V�B��jbr��rG���W���1�-����dp[c��9+q�<�#�w��'�:�Vָ/��Y��#]�s ��zDX�]��k���x*!�$H'�      	   T   x����  �w;�@hSPx9��FQI�&���@7k7�~��`���Y�"�a�.�>9�Q$G�@��q�KL��@�q����     