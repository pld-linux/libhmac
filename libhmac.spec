Summary:	Library to support various Hash-based Message Authentication Codes (HMAC)
Summary(pl.UTF-8):	Biblioteka obsługująca różne kody uwierzytelniające oparte na skrótach (HMAC)
Name:		libhmac
Version:	20150104
Release:	2
License:	LGPL v3+
Group:		Libraries
Source0:	https://github.com/libyal/libhmac/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	884a976f30e374cbdd5ab528d90adca0
Patch0:		%{name}-system-libs.patch
URL:		https://github.com/libyal/libhmac/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcerror-devel >= 20120425
BuildRequires:	libcfile-devel >= 20140503
BuildRequires:	libclocale-devel >= 20120425
BuildRequires:	libcnotify-devel >= 20120425
BuildRequires:	libcpath-devel >= 20120701
BuildRequires:	libcsplit-devel >= 20120701
BuildRequires:	libcstring-devel >= 20120425
BuildRequires:	libcsystem-devel >= 20141018
BuildRequires:	libuna-devel >= 20120425
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 1.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	libcerror >= 20120425
Requires:	libcfile >= 20140503
Requires:	libclocale >= 20120425
Requires:	libcnotify >= 20120425
Requires:	libcpath >= 20120701
Requires:	libcsplit >= 20120701
Requires:	libcstring >= 20120425
Requires:	libcsystem >= 20141018
Requires:	libuna >= 20120425
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libhmac is a library to support various Hash-based Message
Authentication Codes (HMAC).

%description -l pl.UTF-8
libhmac to biblioteka obsługująca różne kody uwierzytelniające oparte
na skrótach (HMAC - Hash-based Message Authentication Codes).

%package devel
Summary:	Header files for libhmac library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libhmac
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcerror-devel >= 20120425
Requires:	libcstring-devel >= 20120425
Requires:	openssl-devel >= 1.0

%description devel
Header files for libhmac library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libhmac.

%package static
Summary:	Static libhmac library
Summary(pl.UTF-8):	Statyczna biblioteka libhmac
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libhmac library.

%description static -l pl.UTF-8
Statyczna biblioteka libhmac.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__sed} -i -e 's/ po\/Makefile.in//' configure.ac
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

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libhmac.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/hmacsum
%attr(755,root,root) %{_libdir}/libhmac.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhmac.so.1
%{_mandir}/man1/hmacsum.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhmac.so
%{_includedir}/libhmac
%{_includedir}/libhmac.h
%{_pkgconfigdir}/libhmac.pc
%{_mandir}/man3/libhmac.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libhmac.a
