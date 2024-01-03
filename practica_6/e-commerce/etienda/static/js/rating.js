document.addEventListener('DOMContentLoaded', () => {
    const ratingElements = document.querySelectorAll('.rating');

    ratingElements.forEach((ratingElement) => {
        ratingElement.innerHTML = `
                                    <span class="fa fa-star"></span>
                                    <span class="fa fa-star"></span>
                                    <span class="fa fa-star"></span>
                                    <span class="fa fa-star not_checked"></span>
                                    <span class="fa fa-star not_checked"></span>
                                    <p><span class="rate"><strong>Rate: </strong></span> <br>
                                    <span class="count"><strong>Count: </strong></span></p>
                                `;

        const stars = ratingElement.querySelectorAll('.fa-star');
        const rateSpan = ratingElement.querySelector('.rate');
        const countSpan = ratingElement.querySelector('.count');

        stars.forEach((star, index) => {
            // Cambiar el color de las estrellas al pasar el ratón por encima
            star.addEventListener('mouseenter', () => {
                stars.forEach((s, i) => {
                    s.classList.toggle('checked', i <= index);
                });
            });

            // Quitar el color de las estrellas al quitar el ratón de encima
            star.addEventListener('mouseleave', () => {
                stars.forEach((s) => {
                    s.classList.remove('checked');
                });
            });

            // Enviar la calificación al API
            star.addEventListener('click', () => {
                // Cambiar el color de las estrellas al ser clicadas
                stars.forEach((s, i) => {
                    s.classList.toggle('checked', i <= index);
                });
                const productId = ratingElement.getAttribute('data-product-id');
                sendRating(productId, index + 1);
            });
        });

        function sendRating(productId, rating) {
            try {
                fetch(`http://localhost:8000/etienda/api/productos/${productId}/rating/${rating}`, {
                    credentials: "same-origin",
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken,
                        'Authorization': 'Basic ' + btoa('admin:admin'),
                    },
                })
                    .then(response => {
                        if (!response.ok) {
                            error = response.status;
                            document.body.appendChild(document.createTextNode("ERROR: " + error));
                            throw new Error('Error al enviar la calificación al API' + error);

                        }
                        return response.json();
                    }).then(data => {
                        document.body.appendChild(document.createTextNode("TODO OK" + JSON.stringify(data)));
                        rateSpan.innerHTML = `<strong>Rate: </strong>${data.rating.rate}`;
                        countSpan.innerHTML = `<strong>Count: </strong>${data.rating.count}`;
                    }).catch(error => {
                        document.body.appendChild(document.createTextNode("ERROR: " + error));
                        console.error('Error:', error);
                    });
            } catch (error) {
                document.body.appendChild(document.createTextNode("ERROR: " + error));
                console.error('Error:', error);
            }
        }
    });
});