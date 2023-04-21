/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ["./views/**/*.ejs"],
  darkMode: "class",
  content: ["./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [require("flowbite/plugin")],
};
