#!/bin/bash
datatime_now="+%Y-%m-%d %H:%M"
git config --global user.name "AWPaulson"
git config --global user.email "wpaulson-ai@ya.ru"
git add *
git commit -m "$datatime_now"
git branch -M main
git remote add origin https://github.com/Caduceus22/crm2911.git
git push -w origin main
