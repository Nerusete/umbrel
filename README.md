## Umbrel Community App Store Template

Este repositorio es una plantilla para crear una tienda de aplicaciones comunitarias de Umbrel. Estas tiendas de aplicaciones adicionales permiten a los desarrolladores distribuir aplicaciones sin necesidad de enviarlas a la tienda oficial de Umbrel. (https://github.com/getumbrel/umbrel-apps).

## How to use:

Cómo usarla:

Comienza haciendo clic en el botón "Usar esta plantilla" que se encuentra arriba.

Asigna un ID y un nombre a tu tienda de aplicaciones en el archivo umbrel-app-store.yml. Este archivo especifica dos atributos importantes:
id: Actúa como un prefijo único para cada aplicación dentro de tu tienda de aplicaciones comunitarias. El ID de tu aplicación debe comenzar con el ID de tu tienda de aplicaciones. Por ejemplo, en esta plantilla, el ID de la tienda de aplicaciones es sparkles y hay una aplicación llamada hello world. Por lo tanto, el ID de la aplicación debería ser: sparkles-hello-world.

name: Este es el nombre de la tienda de aplicaciones comunitarias que se muestra en la interfaz de usuario de umbrelOS.

Cambia el nombre de la carpeta sparkles-hello-world para que coincida con el ID de tu aplicación. Tú decides el ID de la aplicación. Por ejemplo, si el ID de tu tienda de aplicaciones es whistles y tu aplicación se llama My Video Downloader, puedes establecer su ID como whistles-my-video-downloader y renombrar la carpeta en consecuencia.

A continuación, introduce los detalles de tu aplicación en el archivo whistles-my-video-downloader/umbrel-app.yml. Estos se mostrarán en la interfaz de usuario de umbrelOS.

Incluye los servicios Docker necesarios en whistles-my-video-downloader/docker-compose.yml.

¡Listo! Tu tienda de aplicaciones comunitaria, con tu aplicación única, ya está configurada y lista para usar. Para usarla, puedes añadir su URL de GitHub a la interfaz de usuario de umbrelOS, como se muestra en la siguiente demostración:


https://user-images.githubusercontent.com/10330103/197889452-e5cd7e96-3233-4a09-b475-94b754adc7a3.mp4
