-- ===========================================
-- Century Capital — Supabase Database Setup
-- Run this in: supabase.com → Your Project → SQL Editor → New Query
-- ===========================================

-- 1. Contact form submissions (from public website)
create table if not exists contact_submissions (
  id uuid default gen_random_uuid() primary key,
  name text not null,
  email text not null,
  service text,
  budget text,
  message text,
  status text default 'new' check (status in ('new', 'read', 'replied', 'archived')),
  created_at timestamptz default now()
);

-- 2. Projects (client project tracker)
create table if not exists projects (
  id uuid default gen_random_uuid() primary key,
  title text not null,
  client text not null,
  service text,
  status text default 'active' check (status in ('active', 'paused', 'completed', 'cancelled')),
  phase text default 'Discovery' check (phase in ('Discovery', 'Design', 'Development', 'Review', 'Launched')),
  progress_pct integer default 0 check (progress_pct between 0 and 100),
  deadline date,
  value numeric(10,2),
  notes text,
  created_at timestamptz default now()
);

-- 3. Internal messages / notes
create table if not exists messages (
  id uuid default gen_random_uuid() primary key,
  subject text not null,
  body text,
  is_read boolean default false,
  created_at timestamptz default now()
);

-- ===========================================
-- Row Level Security (RLS)
-- ===========================================

-- Enable RLS on all tables
alter table contact_submissions enable row level security;
alter table projects enable row level security;
alter table messages enable row level security;

-- Allow public (anon) to INSERT contact submissions (the form)
create policy "Allow public contact form insert"
  on contact_submissions for insert
  to anon
  with check (true);

-- Allow authenticated users (admin) full access to all tables
create policy "Allow admin full access to contact_submissions"
  on contact_submissions for all
  to authenticated
  using (true)
  with check (true);

create policy "Allow admin full access to projects"
  on projects for all
  to authenticated
  using (true)
  with check (true);

create policy "Allow admin full access to messages"
  on messages for all
  to authenticated
  using (true)
  with check (true);

-- ===========================================
-- Seed Data (demo records)
-- ===========================================

insert into projects (title, client, service, status, phase, progress_pct, deadline, value) values
  ('Brand Identity & Website', 'Apex Materials', 'Brand + Web', 'completed', 'Launched', 100, '2025-03-01', 18000),
  ('E-Commerce Platform', 'Drift Collective', 'E-Commerce', 'active', 'Development', 65, '2026-04-15', 22000),
  ('Patient Portal', 'Serene Health', 'Web + System', 'active', 'Review', 85, '2026-04-01', 35000);

insert into messages (subject, body, is_read) values
  ('Welcome to Century Capital Dashboard', 'This is your admin dashboard. Use it to track projects, view contact enquiries, and manage client communications.', false);
