/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        background: '#050505',
        surface: '#0d0d0d',
        primary: '#f3f4f6',
        secondary: '#9ca3af',
        accent: '#3b82f6',
        'accent-glow': 'rgba(59, 130, 246, 0.15)',
      },
      fontFamily: {
        sans: ['Inter Variable', 'sans-serif'],
        serif: ['Playfair Display', 'serif'],
      },
      boxShadow: {
        'glow-sm': '0 0 10px rgba(255, 255, 255, 0.05)',
        'glow-md': '0 0 20px rgba(59, 130, 246, 0.1)',
        'glow-lg': '0 0 30px rgba(59, 130, 246, 0.2)',
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'noise': "url('/noise.png')",
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-out forwards',
        'float': 'float 6s ease-in-out infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(10px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-10px)' },
        },
      }
    },
  },
  plugins: [],
};
