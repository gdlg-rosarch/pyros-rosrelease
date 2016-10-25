Name:           ros-indigo-pyros
Version:        0.2.0
Release:        1%{?dist}
Summary:        ROS pyros package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       python-six >= 1.5.2
Requires:       ros-indigo-pyros-config >= 0.1.3
Requires:       ros-indigo-pyros-utils >= 0.1.2
Requires:       ros-indigo-pyzmp = 0.0.14
Requires:       ros-indigo-rospy >= 1.11.19
Requires:       ros-indigo-std-msgs >= 0.5.10
Requires:       ros-indigo-std-srvs >= 1.11.2
BuildRequires:  python-mock >= 1.0.1
BuildRequires:  python-six >= 1.5.2
BuildRequires:  ros-indigo-catkin >= 0.6.18
BuildRequires:  ros-indigo-catkin-pip >= 0.1.3
BuildRequires:  ros-indigo-pyros-config >= 0.1.3
BuildRequires:  ros-indigo-pyros-test >= 0.0.3
BuildRequires:  ros-indigo-pyros-utils >= 0.1.2
BuildRequires:  ros-indigo-pyzmp = 0.0.14
BuildRequires:  ros-indigo-rosnode >= 1.11.19
BuildRequires:  ros-indigo-rospy >= 1.11.19
BuildRequires:  ros-indigo-rosservice >= 1.11.19
BuildRequires:  ros-indigo-rostest >= 1.11.19
BuildRequires:  ros-indigo-rostopic >= 1.11.19
BuildRequires:  ros-indigo-rosunit >= 1.11.12

%description
Provides Python to ROS multiprocess API, useful for using ROS from different
multiprocess environment (think webserver, celery, etc.) while keeping both
isolated.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Oct 25 2016 AlexV <asmodehn@gmail.com> - 0.2.0-1
- Autogenerated by Bloom

* Thu Sep 01 2016 AlexV <asmodehn@gmail.com> - 0.2.0-0
- Autogenerated by Bloom

