/** @type {import('tailwindcss').Config} */
import { fontFamily } from 'tailwindcss/defaultTheme';

module.exports = {
	content: ['./templates/**/*.html', './server/**/*.py', './podcaster/templates/**/*.html', './podcaster/**/*.py'],
	theme: {
		extend: {
			fontFamily: {
				sans: ['Inter', ...fontFamily.sans],
			},
			animation: {
				rotate: 'spin 15s linear infinite',
				playing: 'play 30s linear infinite',
			},
		},
	},
	plugins: [require('@tailwindcss/forms')],
};
