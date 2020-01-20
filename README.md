# rpm-application

## Инициализация проекта

```shell script
mkdir -p ~/Repositories/git/rpm-application && cd ~/Repositories/git/rpm-application
```
```shell script
git init
```

```shell script
mvn archetype:generate \
-DgroupId=ru.ezhov.rpm-application \
-DartifactId=application \
-DarchetypeArtifactId=maven-archetype-quickstart \
-DinteractiveMode=false
```
```shell script
echo '# rpm-application' > README.md
```

```shell script
wget -O .gitignore https://raw.githubusercontent.com/github/gitignore/master/Java.gitignore 
echo '.idea' >> .gitignore && echo '*.iml' >> .gitignore && echo 'target' >> .gitignore
```

```shell script
git add .gitignore && git add README.md & git add application  
```

```shell script
mvn clean package
```

```shell script
java -cp application/target/application-1.0.jar ru.ezhov.rpm.application.App
```

## Сборка проекта с использованием RPM
Цель: 
> Собрать из приложения готовый для установки RPM пакет

Действия, которые необходимо сделать для установки приложения
1. Создание папки **/opt/rpm-application**
1. Расположение файла запуска **rpmtest** в **/usr/bin**
1. Запуск приложения из командной строки командой **rpmtest** 

```shell script
sudo apt-get install rpm
sudo apt-get install alien
```
```shell script
mkdir -p ~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
```

```shell script
mvn clean package -f application/pom.xml
```

```shell script
cp application/target/application-1.0.jar ~/rpmbuild/SOURCES/ && 
mkdir -p ~/rpmbuild/BUILDROOT/rpm-application-1.0-1.x86_64 &&
mkdir -p ~/rpmbuild/BUILDROOT/rpm-application-1.0-1.x86_64/opt/rpm-application &&
mkdir -p ~/rpmbuild/BUILDROOT/rpm-application-1.0-1.x86_64/usr/bin &&
cp rpmtest ~/rpmbuild/BUILDROOT/rpm-application-1.0-1.x86_64/usr/bin/rpmtest &&
chmod 755 ~/rpmbuild/BUILDROOT/rpm-application-1.0-1.x86_64/usr/bin/rpmtest &&
cp application/target/application-1.0.jar ~/rpmbuild/BUILDROOT/rpm-application-1.0-1.x86_64/opt/rpm-application/ &&
rpmbuild -bb rpm_application.spec
```

```shell script
sudo alien -i ~/rpmbuild/RPMS/x86_64/rpm-application-1.0-1.x86_64.rpm
```
или
```shell script
sudo rpm -i ~/rpmbuild/RPMS/x86_64/rpm-application-1.0-1.x86_64.rpm 
```
