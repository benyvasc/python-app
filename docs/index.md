# Test TechDocs on Backstage
## 1. Obtendo código fonte:
- https://backstage.io/docs/getting-started/#prerequisites
- Necessário: Node (v22 ou v24), NVM, Yarn
- Download com NPX:
> npx @backstage/create-app@latest

## 2. Configurando autenticação:
- Escolher um `authentication provider`, como Gitlab, GitHUB.
- Para GitHUB use as configurações deste link:
    - https://backstage.io/docs/auth/github/provider

### Gerando uma credencial para integração.
- Nas configuração do seu usuário acesse settings:
- Em https://github.com/settings/profile > Developer Settings > OAuth Apps e crie um New OAuth App

- Para acessar a aplicação com Docker, o ajuste abaixo tem que ser feito no `app-config.yaml`.

```
app:
  title: Scaffolded Backstage App
  baseUrl: http://localhost:3000
  listen:
    host: 0.0.0.0
```
### Backend Installation
- Na pasta do projeto instale a lib com:
> yarn --cwd packages/app add @backstage/core-plugin-api @backstage/plugin-app-react

- Edite packages/backend/src/index.ts incluindo:
```
backend.add(import('@backstage/plugin-auth-backend-module-github-provider'));
```

### Adding the provider to the Backstage frontend
- Edite packages/app/src/App.tsx incluido:
- Ver documentação.

### Ajuste o resolver
- Necessário para definir que terá permissão depois da autenticação.
- https://github.com/backstage/backstage/tree/master/packages/catalog-model/examples/acme

## 3. Funcionalidades
Backstage  trabalha sobre 3 pilares
- Software Catalog
  - https://backstage.io/docs/features/software-catalog/descriptor-format/
  - https://backstage.io/docs/features/software-catalog/descriptor-format/#kind-component
- TechDocs
    - Usa mkdocs
    - https://github.com/backstage/backstage/blob/master/mkdocs.yml
- Software templates