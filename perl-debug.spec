#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	debug
Summary:	Perl pragma for debugging and logging of debug lines
Summary(pl.UTF-8):	Pakiet Perla do śledzenia i logowania linii diagnostycznych
Name:		perl-debug
Version:	0.03
Release:	0.1
# same as perl
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/S/ST/STEVAN/debug-%{version}.tar.gz
# Source0-md5:	2648f7e792445ba4b6bc42a56924a708
URL:		http://search.cpan.org/dist/debug/
%if %{with tests}
BuildRequires:	perl-Test-Pod >= 1.14
BuildRequires:	perl-Test-Pod-Coverage >= 1.04
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The debug pragma provides a very simple way of turning on and off your
debugging lines, as well as a very flexible way of logging those lines
to literally anywhere you want.

%description -l pl.UTF-8
Pakiet debug udostępnia bardzo prosty sposób włączania i wyłączania
linii diagnostycznych, a także bardzo elastyczny sposób logowania tych
linii dosłownie wszędzie, gdzie chcemy.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/debug.pm
%{_mandir}/man3/*
