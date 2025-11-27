const supabaseUrl = import.meta.env.SUPABASE_URL;
const supabaseAnonKey = import.meta.env.SUPABASE_ANON_KEY;

console.log('Supabase URL:', supabaseUrl); // Debug log
console.log('Has anon key:', !!supabaseAnonKey); // Debug log (don't log the actual key)

if (!supabaseUrl || !supabaseAnonKey) {
    console.error('Missing Supabase environment variables');
    throw new Error('Supabase configuration is missing');
}

export const supabase = window.supabase.createClient(supabaseUrl, supabaseAnonKey);