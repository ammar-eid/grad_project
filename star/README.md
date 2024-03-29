
# AutoPentest-DRL: Automated Penetration Testing Using Deep Reinforcement Learning

AutoPentest-DRL is an automated penetration testing framework based on
Deep Reinforcement Learning (DRL) techniques. AutoPentest-DRL can
determine the most appropriate attack path for a given logical
network, and can also be used to execute a penetration testing attack
on a real network via tools such as Nmap and Metasploit. This
framework is intended for educational purposes, so that users can
study the penetration testing attack mechanisms. AutoPentest-DRL is
being developed by the Cyber Range Organization and Design
([CROND](https://www.jaist.ac.jp/misc/crond/index-en.html))
NEC-endowed chair at the Japan Advanced Institute of Science and
Technology ([JAIST](https://www.jaist.ac.jp/english/)) in Ishikawa,
Japan.

An overview of AutoPentest-DRL is shown below. The framework receives
user input regarding the logical target network, including
vulnerability information; alternatively, the framework can use Nmap
for network scanning to find actual vulnerabilities in a real target
network with known topology. The MulVAL attack-graph generator is then
used to determine potential attack trees, which are fed in a
simplified form into the DQN Decision Engine. The attack path that is
produced as output can be used to study the attack mechanisms on a
large number of logical networks. Alternatively, the framework can use
the attack path with penetration testing tools, such as Metasploit,
making it possible for the user to study how the attack can be carried
out on a real target network.

![Overview of AutoPentest-DRL](/Figures/framework_overview.png?raw=true "Overview of AutoPentest-DRL")

Next we provide brief information on how to setup and use
AutoPentest-DRL. For details about its operation, please refer to the
[User Guide](/user_guide.md) that we also make available.


## Prerequisites

Several external tools are required in order to use AutoPentest-DRL;
for the basic functionality (DQN training and attacks on logical
networks), you'll need:
* **MulVAL**: Attack-graph generator used by AutoPentest-DRL to
  produce possible attack paths for a given network. See the [MulVAL
  page](https://github.com/risksense/mulval) for installation
  instructions and dependencies. MulVAL should be installed in the
  directory `repos/mulval` in the AutoPentest-DRL folder. You also
  need to configure the `/etc/profile` file as discussed
  [here](https://www.programmersought.com/article/37794643490/). On
  some systems the tool `epstopdf` may also need to be installed, for
  instance by using the command below:
  ```
  sudo apt install texlive-font-utils
  ```

If you plan to use AutoPentest-DRL with real networks, you'll also
need:
* **Nmap**: Network scanner used by AutoPentest-DRL to determine 
  vulnerabilities in a given real network. The command needed to
  install `nmap` on Ubuntu is given below:
  ```
  sudo apt install nmap
  ```
* **Metasploit**: Penetration testing tools used by AutoPentest-DRL to
  actually conduct the attack proposed by the DQN engine on the real
  target network. To install Metasploit, you can use the installers
  made available on the [Metasploit
  website](https://www.metasploit.com/). In addition, we use
  `pymetasploit3` as RPC API to communicate with Metasploit, and this
  tool needs to be installed in the directory
  `Penetration_tools/pymetasploit3` by following its author's
  [instructions](https://github.com/DanMcInerney/pymetasploit3).


## Setup

AutoPentest-DRL has been developed mainly on the Ubuntu 18.04 LTS
operating system; other OSes may work, but have not been tested. In
order to set up AutoPentest-DRL, use the
[releases](https://github.com/crond-jaist/AutoPentest-DRL/releases)
page to download the latest version, and extract the source code
archive into a directory of your choice (for instance, your home
directory) on the host on which you intend to use it.

AutoPentest-DRL is implemented in Python, and it requires several
packages to run. The file `requirements.txt` included with the
distribution can be used to install the necessary packages via the
following command that should be run from the `AutoPentest-DRL/`
directory:
```
$ sudo -H pip install -r requirements.txt
```


## Quick Start

AutoPentest-DRL includes a trained DQN model, so you can use it
out-of-the-box on a sample logical network topology by running the
following command in a terminal from the `AutoPentest-DRL/` directory:
```
$ python3 ./AutoPentest-DRL.py logical_attack
```

In this **logical attack mode** no actual attack is conducted, and
AutoPentest-DRL will only determine the optimal attack path for the
logical network topology that is described in the file
`MulVal_P/logical_attack_v1.P`. By comparing the output path with the
visualization of the attack graph that is generated by MulVAL in the
file `mulval_results/AttackGraph.pdf` you can study in detail the
attack steps.

For more information about the operation of AutoPentest-DRL, including
the **real attack mode** to be used when conducting penetration
testing on real networks, see our [User Guide](/user_guide.md).


## References

For a research background regarding AutoPentest-DRL, please refer to
the following references:

* Z. Hu, R. Beuran, Y. Tan, "Automated Penetration Testing Using Deep
  Reinforcement Learning", IEEE European Symposium on Security and
  Privacy Workshops (EuroS&PW 2020), Workshop on Cyber Range
  Applications and Technologies (CACOE'20), Genova, Italy, September
  7, 2020, pp. 2-10.
* Z. Hu, "Automated Penetration Testing Using Deep Reinforcement
  Learning", Master's thesis,
  March 2021. https://hdl.handle.net/10119/17095

For a list of contributors to this project, see the file CONTRIBUTORS
included in the distribution.
