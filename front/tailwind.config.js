/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        'custom-pink': '#F8ACFF',
        'custom-blue': '#7DD3FC',
      },
      fontFamily: {
        hahmlet: ['Hahmlet', 'serif'],
      },
      backgroundImage: {
        'error-page': "url('./public/images/bg/error-bg.png')",
      },
      keyframes: {
        glitch: {
          '0%, 100%': { clip: 'rect(0, 9999px, 0, 0)' },
          '10%': {
            clip: 'rect(50px, 9999px, 80px, 0)',
            transform: 'translate(-2px, -2px)',
          },
          '20%': {
            clip: 'rect(85px, 9999px, 150px, 0)',
            transform: 'translate(1px, 1px)',
          },
          '30%': {
            clip: 'rect(30px, 9999px, 60px, 0)',
            transform: 'translate(-1px, 1px)',
          },
          '40%': {
            clip: 'rect(60px, 9999px, 120px, 0)',
            transform: 'translate(1px, -1px)',
          },
          '50%': {
            clip: 'rect(20px, 9999px, 100px, 0)',
            transform: 'translate(0, 0)',
          },
          '60%': {
            clip: 'rect(90px, 9999px, 140px, 0)',
            transform: 'translate(1px, 1px)',
          },
          '70%': {
            clip: 'rect(10px, 9999px, 40px, 0)',
            transform: 'translate(-1px, -1px)',
          },
          '80%': {
            clip: 'rect(80px, 9999px, 130px, 0)',
            transform: 'translate(1px, -1px)',
          },
          '90%': {
            clip: 'rect(40px, 9999px, 70px, 0)',
            transform: 'translate(-1px, 1px)',
          },
        },
        slideIn: {
          '0%': { transform: 'translateX(100%)' },
          '100%': { transform: 'translateX(0)' },
        },
        slideOut: {
          '0%': { transform: 'translateX(0)' },
          '100%': { transform: 'translateX(100%)' },
        },
        fadeIn: {
          '0%': { opacity: 0 },
          '100%': { opacity: 1 },
        },
        fadeOut: {
          '0%': { opacity: 1 },
          '100%': { opacity: 0 },
        },
      },
      animation: {
        glitch: 'glitch 0.3s infinite',
        slideIn: 'slideIn 0.5s forwards',
        slideOut: 'slideOut 0.5s forwards',
        fadeIn: 'fadeIn 0.5s forwards',
        fadeOut: 'fadeOut 0.5s forwards',
      },
    },
  },
  plugins: [],
};
