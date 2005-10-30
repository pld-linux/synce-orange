
%define	_realname	orange

Summary:	SynCE Orange - a tool capable to get installable MS Cabinet Files from installers
Summary(pl):	SynCE Orange - narzêdzie zdolne do wydobycia plików MS Cabinet z instalatorów
Name:		synce-%{_realname}
Version:	0.3
Release:	1
License:	MIT
Group:		Applications
Source0:	http://dl.sourceforge.net/synce/%{_realname}-%{version}.tar.gz
# Source0-md5:	90f6e822bb81af886dce5bdecd227655
URL:		http://synce.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.4
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	synce-libsynce-devel
BuildRequires:	synce-dynamite-libs-devel
BuildRequires:	synce-unshield-libs-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Orange is a tool for squeezing out juicy installable Microsoft Cabinet
Files from self-extracting installers for Microsoft Windows and some
other installer file formats.

%description -l pl
Orange jest narzêdziem umo¿liwiaj±cym wydobycie z samorozpakowuj±cych
siê instalatorów przeznaczonych dla Microsoft Windows plików Microsoft
Cabinet.

%package libs
Summary:	The Orange library
Summary(pl):	Biblioteka Orange
Group:		Libraries

%description libs
The Orange library.

%description libs -l pl
Biblioteka Orange.

%package libs-devel
Summary:	Header files for the Orange library
Summary(pl):	Pliki nag³ówkowe biblioteki Orange
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description libs-devel
Header files for the Orange library.

%description libs-devel -l pl
Pliki nag³ówkowe biblioteki Orange.

%package libs-static
Summary:	Static Orange library
Summary(pl):	Statyczna biblioteka Orange
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description libs-static
Static Orange library.

%description libs-static -l pl
Statyczna biblioteka Orange.

%prep
%setup -q -n %{_realname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liborange.so.*.*.*

%files libs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liborange.so
%{_libdir}/liborange.la
%{_includedir}/liborange.h

%files libs-static
%defattr(644,root,root,755)
%{_libdir}/liborange.a
