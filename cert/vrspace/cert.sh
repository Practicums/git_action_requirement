gcloud container clusters get-credentials vrspace-cluster
kubectl delete secret vrspace-tls 2> /dev/null
chmod +x /home/metaverseops/project/vrspace/git_action_requirement/cert/vrspace/cert-manager_install.sh && /home/metaverseops/project/vrspace/git_action_requirement/cert/vrspace/cert-manager_install.sh
export EMAIL=metaverse-serv@metaverse-363005.iam.gserviceaccount.com
cat /home/metaverseops/project/vrspace/git_action_requirement/cert/vrspace/letsencrypt-issuer.yaml | sed -e "s/email: ''/email: $EMAIL/g" | kubectl apply -f-