# Custos Frontend
The frontend of custos will be an admin panel to manage all services and moderate users.

The tech-stack of the frontend is purely Nuxt.

Most UI is using `NuxtUI`, for an overview of components see the [documentation here](https://ui.nuxt.com/components).

## Local Setup
You need to have `Node` installed to work in this repository.

To start the local development server.
```bash
# install dependencies (once)
pnpm install

# start development server
pnpm dev
```

### Promo Mode
The UI can be launched in "promoMode", meaning it is used for presenting custos features.

To start custos in "promoMode", simply run `pnpm dev:promo` which, in the background, sets a runtimeConfig variable to true.

## Build Website
To build the website run the following command. You'll receive static files that can be deployed on any Web-host.
```
pnpm generate
```

## Icons
To search for icons use [this page](https://icon-sets.iconify.design/lucide/) and add a prefix of `lucide-` to the icon name.

---
Check out the [Nuxt documentation](https://nuxt.com/docs/getting-started/introduction) to learn more.
