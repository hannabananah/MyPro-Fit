/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        'custom-pink': '#F8ACFF',
        'custom-blue': '#7DD3FC',
      },
    },
  },
  plugins: [],
};
