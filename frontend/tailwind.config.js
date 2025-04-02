/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          blue: '#0A164F',
          midblue: '#102B7D',
          pink: '#FF3CAC',
          yellow: '#F9DC5C',
        },
      },
      fontFamily: {
        sans: ['"Titillium Web"', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
