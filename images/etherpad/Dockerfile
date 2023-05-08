FROM etherpad/etherpad

USER root

COPY ./ep_oauth2-0.2.0.tgz /tmp/ep_oauth2.tgz
RUN npm install --no-save --legacy-peer-deps \
        ep_align \
        ep_embedded_hyperlinks2 \
        ep_font_color \
        ep_headings2 \
        ep_markdown \
        ep_image_upload \
        ep_openid_connect \
        /tmp/ep_oauth2.tgz \
    && src/bin/installDeps.sh \
    && rm -rf ~/.npm

USER etherpad
