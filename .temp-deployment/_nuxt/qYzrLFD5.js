import{_,a as f}from"./BXGPYLEM.js";import{_ as x}from"./BmqJo3xs.js";import{_ as g}from"./BiHTBc_E.js";import{_ as P}from"./CxHsmPvU.js";import{i as w,r as b,h as y,c as v,o as C,a,b as n,w as r,p as s,n as V}from"./C5MHcV20.js";const k=`services:
  custos:
    image: glitchdevx/custos:latest
    restart: always
    ports:
      - "127.0.0.1:<<BACKEND_PORT>>:3060"
    volumes:
      - type: bind
        source: custos-config
        target: /config
<<UI_PART>>volumes:
  custos:`,U=`  custos-ui:
    image: glitchdevx/custos-ui:latest
    restart: always
    depends_on:
      - custos
    ports:
      - "127.0.0.1:<<FRONTEND_PORT>>:80"`,N={id:"get-started",class:"flex justify-center items-center"},O={class:"w-3xl max-w-full"},R={class:"flex flex-row gap-2 mt-4 max-sm:flex-col"},T=w({__name:"GetStarted",setup(B){const e=b({ui:!0,backendPort:3060,frontendPort:3070}),i=y(()=>{let o=k;const t=e.ui?U+`
`:"";return o=o.replace("<<UI_PART>>",t),o=o.replace("<<BACKEND_PORT>>",e.backendPort.toString()),o=o.replace("<<FRONTEND_PORT>>",e.frontendPort.toString()),o});return(o,t)=>{const d=_,c=f,m=x,u=g,p=P;return C(),v("div",N,[a("div",O,[t[4]||(t[4]=a("div",{class:"max-w-xl"},[a("h2",{class:"text-3xl font-bold"}," Start with Docker Compose "),a("p",{class:"muted-text"}," You can start off by simply creating a new directory with a docker-compose.yaml and this content. ")],-1)),a("div",R,[n(u,{class:"max-sm:flex max-sm:justify-center"},{default:r(()=>[t[3]||(t[3]=a("span",{class:"text-xl font-bold"}," Configure Compose ",-1)),n(d,{modelValue:s(e).ui,"onUpdate:modelValue":t[0]||(t[0]=l=>s(e).ui=l),label:"User Interface",class:"mt-4"},null,8,["modelValue"]),n(m,{label:"Backend Port",class:"mt-4"},{default:r(()=>[n(c,{modelValue:s(e).backendPort,"onUpdate:modelValue":t[1]||(t[1]=l=>s(e).backendPort=l),orientation:"vertical",formatOptions:{useGrouping:!1,style:"decimal"}},null,8,["modelValue"])]),_:1}),n(m,{label:"Frontend Port",class:V(["mt-2",{"low-opacity":!s(e).ui}])},{default:r(()=>[n(c,{modelValue:s(e).frontendPort,"onUpdate:modelValue":t[2]||(t[2]=l=>s(e).frontendPort=l),orientation:"vertical",formatOptions:{useGrouping:!1,style:"decimal"}},null,8,["modelValue"])]),_:1},8,["class"])]),_:1}),n(p,{content:s(i),showCopy:!0,language:"yaml",class:"max-w-[500px] grow"},null,8,["content"])])])])}}}),h=Object.assign(T,{__name:"HomeGetStarted"});export{h as default};
