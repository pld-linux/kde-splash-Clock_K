
%define		_splash		Clock_K

Summary:	KDE splash screen
Summary(pl):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Amusements
#Source0:	http://www.kde-look.org/content/download.php?content=15944&id=1
Source0:	http://www.kde-look.org/content/files/15944-Clock_K.tar.gz
# Source0-md5:	dc52fc91987ba40a7a34a824d11dd970
URL:		http://www.kde-look.org/content/show.php?content=15944
Provides:	kde-splash
Requires:	kdebase-desktop >= 9:3.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Your KDE may now start ticking :) Splash with clock made of KDE logo.

%description -l pl
Twoje KDE mo¿e teraz zacz±æ tykaæ :) Ekran startowy z logo KDE
przerobionym na zegarek.

%prep
%setup -q -n %{_splash}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}
install * $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/*
