Name: rpm-application
Version: 1.0
Release: 1

Summary: test application
Summary(ru): тестовое приложение
License: Simple
URL: https://github.com/ezhov-da

%description
Test application

%description -l ru
Тестовое приложение

%pre
if [[ not -d "/opt/rpm-application" ]]; then
    mkdir /opt/rpm-application
fi

%files
/opt/rpm-application
/usr/bin/rpmtest

%changelog