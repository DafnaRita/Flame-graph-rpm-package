Name:           shell-script
Version: 		0.1
Release:        0
Summary:        shell-script

Requires: tomcat
Requires: cmake 
Requires: perf 
Requires: java-1.8.0-openjdk-headless-debug

Group:          Test
Source0: shell-script-%{version}.tar.gz
License: OtherLicense

%description
Package to pass a checkpoint number 3

%prep
%setup

%build
ls -la
cd perf-map-agent
cmake .
make 
cd ..

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
mkdir -p ${RPM_BUILD_ROOT}/usr/lib/jvm/perf-map-agent
mkdir -p ${RPM_BUILD_ROOT}/usr/lib/jvm/FlameGraph
install -m 755 shell-script.sh ${RPM_BUILD_ROOT}/usr/bin
cp -r perf-map-agent ${RPM_BUILD_ROOT}/usr/lib/jvm
cp -r FlameGraph ${RPM_BUILD_ROOT}/usr/lib/jvm

%post
echo "post begin"
echo "export JAVA_OPTS='-Djava.awt.headless=true -Xmx1024m -XX:+UseG1GC -XX:+PreserveFramePointer -XX:+UnlockDiagnosticVMOptions -XX:+DebugNonSafepoints'" >> /etc/profile
export JAVA_OPTS='-Djava.awt.headless=true -Xmx1024m -XX:+UseG1GC -XX:+PreserveFramePointer -XX:+UnlockDiagnosticVMOptions -XX:+DebugNonSafepoints'
echo "post end"

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/shell-script.sh
%attr(755,root,root) /usr/lib/jvm

%changelog
