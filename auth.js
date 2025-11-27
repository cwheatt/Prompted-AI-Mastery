const supabaseUrl = "https://tisxbfdljpjyptrlbrkb.supabase.co";
const supabaseAnonKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRpc3hiZmRsanBqeXB0cmxicmtiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjI2NjYzMzcsImV4cCI6MjA3ODI0MjMzN30.ToLI0L-CihtcNNZnr7tY1JxO-fGgPZKsIdet1ScJbOY";

console.log('Supabase initialized');

export const supabase = window.supabase.createClient(supabaseUrl, supabaseAnonKey);
