document.addEventListener('DOMContentLoaded', () => {
	const btn = document.getElementById('btnAcessar');
	const seletor = document.getElementById('seletorSite');
	const resultado = document.getElementById('resultado');

	btn.addEventListener('click', navegar);

	// Permitir Enter quando o select estiver focado
	seletor.addEventListener('keydown', (e) => {
		if (e.key === 'Enter') navegar();
	});

	function navegar() {
		const url = seletor.value;
		if (!url) {
			resultado.textContent = 'Por favor, selecione um site.';
			resultado.classList.add('error');
			return;
		}

		resultado.textContent = `Abrindo ${seletor.options[seletor.selectedIndex].text}...`;
		resultado.classList.remove('error');
		window.open(url, '_blank');
	}
});
